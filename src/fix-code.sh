#!/bin/bash

# List all Python files tracked by Git
FILES=$(git ls-files '*.py')

# Run Black, isort, and Flake8 on each file
for FILE in $FILES; do
    black "$FILE"
    isort "$FILE"
    flake8 "$FILE"
done

# Optionally, run pylint to show remaining issues
pylint $FILES