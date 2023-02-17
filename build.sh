#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip 
poetry install

python manage.py collectstatic --no-input
python manage.py migrate