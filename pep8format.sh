#!/usr/bin/env bash

python_files=$(find -iname '*.py')

for file in $python_files; do
  autopep8 -ia $file
done
