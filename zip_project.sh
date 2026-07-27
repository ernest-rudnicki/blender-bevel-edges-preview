#!/bin/bash

BUILD_DIRECTORY="./build"
COMPRESSED_FILE_PATH="$BUILD_DIRECTORY/bevel.edge_preview.zip"
PROJECT_FOLDER="./bevel_edge_preview/"

mkdir -p $BUILD_DIRECTORY
if [ -e $COMPRESSED_FILE_PATH ]
then
    echo "Removing old build..."
    rm -rf $COMPRESSED_FILE_PATH
fi

python -m zipfile -c $COMPRESSED_FILE_PATH $PROJECT_FOLDER
echo "Build completed successfully"
