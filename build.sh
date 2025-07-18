#!/bin/bash

# Build script for Allegro Hand ZMQ Interface
# Based on "Installing this interface" section in README.md

set -e  # Exit on any error

echo "Building Allegro Hand ZMQ Interface..."

# The CMakeLists.txt is in the root directory, not cpp
# Create build directory if it doesn't exist
if [ ! -d "build" ]; then
    echo "Creating build directory..."
    mkdir build
fi

# Navigate to build directory
cd build

# Run cmake from root directory
echo "Running cmake..."
cmake ..

# Build the project
echo "Building the project..."
make

# Install the project
echo "Installing the project..."
make install

echo "Build completed successfully!"