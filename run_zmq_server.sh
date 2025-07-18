#!/bin/bash

# Script to run the Allegro Hand ZMQ server
# Executes the grasp binary built by build.sh

set -e  # Exit on any error

echo "Starting Allegro Hand ZMQ server..."

# Check if grasp binary exists
if [ ! -f "build/bin/grasp" ]; then
    echo "Error: grasp binary not found at build/bin/grasp"
    echo "Please run ./build.sh first to build the project"
    exit 1
fi

# Execute the grasp binary
echo "Running grasp server..."
./build/bin/grasp