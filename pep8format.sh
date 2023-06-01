#!/usr/bin/env bash

python_files=$(find -iname '*.py')

for file in $python_files; do
  printf '%s\n' $file
  autopep8 -ia $file
done
