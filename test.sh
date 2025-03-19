#!/bin/bash
echo "Running tests..."

# Run unit tests
echo "Running unit tests..."
pytest tests/unit/ --maxfail=1 --disable-warnings -q  # Specify the path to unit tests

# Check the result of unit tests
if [ $? -ne 0 ]; then
    echo "Unit tests failed!"
    exit 1
fi

# Run integration tests
echo "Running integration tests..."
pytest tests/integration/ --maxfail=1 --disable-warnings -q  # Specify the path to integration tests

# Check the result of integration tests
if [ $? -ne 0 ]; then
    echo "Integration tests failed!"
    exit 1
fi

echo "All tests passed!"
