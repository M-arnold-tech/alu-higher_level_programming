#!/bin/bash

# Ensure PYFILE environment variable is set
if [ -z "$PYFILE" ]; then
    echo "Error: PYFILE environment variable is not set."
    exit 1
fi

# Compile the Python script
OUTPUT_FILE="${PYFILE}c"
echo "Compiling $PYFILE ..."
python3 -m py_compile "$PYFILE"

# Move the compiled file to match the required output name
COMPILED_FILE="__pycache__/$(basename "$PYFILE" .py).cpython-*.pyc"
if ls $COMPILED_FILE 1> /dev/null 2>&1; then
    mv $COMPILED_FILE "$OUTPUT_FILE"
else
    echo "Compilation failed."
    exit 1
fi

