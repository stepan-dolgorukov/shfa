#!/usr/bin/env bash

/usr/bin/python3 -m coverage run -m unittest discover -s test -p 'test_*.py' &&
/usr/bin/python3 -m coverage report
