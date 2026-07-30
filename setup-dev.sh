#!/usr/bin/env bash
set -euo pipefail

VENV_DIR=".venv"
REQUIREMENTS_FILE="requirements-dev.txt"

find_python() {
    if command -v python >/dev/null 2>&1; then
        command -v python
        return
    fi

    if command -v python3 >/dev/null 2>&1; then
        command -v python3
        return
    fi

    if command -v py >/dev/null 2>&1; then
        command -v py
        return
    fi

    echo "Python was not found. Install Python or add it to PATH." >&2
    exit 1
}

PYTHON_COMMAND="$(find_python)"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    "$PYTHON_COMMAND" -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

if [ -x "$VENV_DIR/Scripts/python.exe" ]; then
    VENV_PYTHON="$VENV_DIR/Scripts/python.exe"
elif [ -x "$VENV_DIR/bin/python" ]; then
    VENV_PYTHON="$VENV_DIR/bin/python"
else
    echo "Could not find Python inside $VENV_DIR." >&2
    exit 1
fi

echo "Upgrading pip..."
"$VENV_PYTHON" -m pip install --upgrade pip

echo "Installing development requirements..."
"$VENV_PYTHON" -m pip install -r "$REQUIREMENTS_FILE"

echo "Development environment is ready."
echo "Interpreter: $VENV_PYTHON"
