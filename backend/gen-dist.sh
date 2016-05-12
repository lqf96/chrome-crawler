#! /bin/sh

cd $(dirname $0)
# Generate source distribution
./setup.py sdist >/dev/null 2>&1
# Copy distribution to "dist" folder
for dist_file in dist/*.tar.gz; do
    mv $dist_file ../dist
    ln -f ../dist/$(basename $dist_file) ../dist/latest.tar.gz
done
# Clean up
rm -rf ChromeCrawler.egg-info dist >/dev/null 2>&1
