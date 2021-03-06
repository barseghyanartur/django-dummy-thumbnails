#!/usr/bin/env bash
#./scripts/uninstall.sh
#./scripts/install.sh
./scripts/prepare_docs.sh

sphinx-build -n -a -b html docs builddocs
sphinx-build -n -a -b rinoh docs builddocs
cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..
