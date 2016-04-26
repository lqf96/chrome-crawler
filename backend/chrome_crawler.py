""" Chrome crawler backend server. """

# Python language features
from __future__ import unicode_literals, print_function
# Gevent
from gevent import sleep, monkey
monkey.patch_all()
# Bottle.py
from bottle import Bottle, request as req, response as res, redirect, static_file, abort
# Python system libraries
import json, sys
from collections import deque
from base64 import b64encode, b64decode
from urllib import quote, unquote
from os.path import dirname, abspath
from copy import copy
from pkg_resources import Requirement, resource_string
from mimetypes import guess_type

# Package name
_pkg_name = Requirement.parse("ChromeCrawler")

# Chrome crawler backend
class ChromeCrawler(object):
    """ Chrome crawler backend server class. """
    # [ Backend Routes ]
    # Receive message from browser
    def _recv_msg(self):
        """ Route for sending message to backend. """
        # Get message data
        msg_data = json.loads(unquote(b64decode(req.params.data)))
        # Trigger correspond event
        callbacks = self._callback.get(msg_data["event"])
        if callbacks:
            for callback in callbacks:
                callback(msg_data["data"])
        # Message received
        res.set_header(b"content-type", b"application/json")
        return json.dumps({"status": "success"})
    # Client side message subscription
    # (Used to push message to client)
    def _msg_polling(self):
        """ Front-end message polling route. """
        # Set content type
        res.set_header(b"content-type", b"text/event-stream")
        # Send response header
        yield "retry: 2000\n\n"
        # Polling loop
        while True:
            # Check message sending queue
            while self._msg_queue:
                current_msg = self._msg_queue.popleft()
                yield "data: "+b64encode(quote(json.dumps(current_msg)))+"\n\n"
            sleep(0)
    # Server side routes
    def _bknd_config(self):
        """ Return backend configuration. """
        res.set_header(b"content-type", b"application/json")
        return json.dumps(self.conf)
    # [ Static Routes ]
    # Index redirection
    @staticmethod
    def _index_redirect():
        """ Index redirection route. """
        redirect("/index.html")
    # Static files
    @staticmethod
    def _crawler_static(path):
        """ Serve Chrome crawler static files. """
        # Fetch file content
        try:
            file_content = resource_string(_pkg_name, "frontend/"+path)
        except IOError:
            abort(404, "Not Found")
        # Guess MIME type from file name
        mime_type = guess_type(path)[0]
        if mime_type:
            res.set_header(b"content-type", mime_type)
        # Return file content
        return file_content
    # Custom static files
    def _custom_static(self, path):
        """ Serve custom script & files. """
        return static_file(path, root=self.conf["custom_root"])
    # [ Member Functions ]
    # Constructor
    def __init__(self, **kwargs):
        """
        Constructor of the Chrome crawler backend.

        Possible configuration items include:
        * custom_root: Custom script root folder. (Will be mounted at "/custom")
        * entry: Custom script entry point.
        """
        # Members
        self._msg_queue = deque()
        self._callback = {}
        self.conf = copy(kwargs)
        # Bottle.py web app
        self.app = Bottle()
        # Backend routes
        self.app.route("/bknd/msg", method="POST", callback=self._recv_msg)
        self.app.route("/bknd/poll", callback=self._msg_polling)
        self.app.route("/bknd/config", callback=self._bknd_config)
        # Static files
        self.app.route("/", callback=ChromeCrawler._index_redirect)
        if "custom_root" in kwargs:
            self.app.route("/custom/<path:path>", callback=self._custom_static)
        self.app.route("/<path:path>", callback=ChromeCrawler._crawler_static)
    # Run application
    def run(self, **kwargs):
        """ Run backend server with given Bottle.py arguments. """
        # Running prompt
        print("Please close all Chrome windows, and then rerun Chrome with following flags:")
        print("google-chrome --disable-web-security --user-data-dir")
        print()
        # Start browser
        self.app.run(server="gevent", debug=True, **kwargs)
    # Add event handler
    def on(self, event, handler=None):
        """
        Add a callback to handler events from client side.
        The callback can be added either in classical or in decorator style.
        """
        # Classical style
        if handler:
            event_handlers = self._callback.setdefault(event, [])
            event_handlers.append(handler)
            return handler
        # Decorator style
        else:
            return lambda _handler: self.on(event, _handler)
    # Send message to client
    def emit(self, event, data):
        """ Send a message with given event type to client. """
        self._msg_queue.append({"event": event, "data": data})
