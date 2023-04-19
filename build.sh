#!/bin/sh
python setup.py --quiet develop
python setup.py --quiet sdist bdist_wheel
