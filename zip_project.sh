#!/bin/bash

BUILD_DIRECTORY="./build"
PROJECT_FOLDER="./bevel_edge_preview"
COMPRESSED_FILE_PATH="$BUILD_DIRECTORY/bevel.edge_preview.zip"
VERSION=$(grep '"version"' "$PROJECT_FOLDER/__init__.py" | grep -oP '"version"\s*:\s*\(\K[0-9,\s]+(?=\))' | tr -d ' ' | tr ',' '.')

cp "./LICENSE" "$PROJECT_FOLDER"
cp "./README.md" "$PROJECT_FOLDER"
echo "Version: $VERSION" > "$PROJECT_FOLDER/version.txt"

mkdir -p "$BUILD_DIRECTORY"
if [ -e "$COMPRESSED_FILE_PATH" ]
then
    echo "Removing old build..."
    rm -rf "$COMPRESSED_FILE_PATH"
    echo "Old build removed successfully"
fi

python -m zipfile -c "$COMPRESSED_FILE_PATH" "$PROJECT_FOLDER"

echo "Removing temporary files..."
rm -rf "$PROJECT_FOLDER/version.txt"
rm -rf "$PROJECT_FOLDER/LICENSE"
rm -rf "$PROJECT_FOLDER/README.md"
echo "Temporary files removed successfully"

echo "Build completed successfully"
