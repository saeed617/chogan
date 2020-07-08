#!/bin/bash
set -e

./manage.py makemigrations
./manage.py migrate
./manage.py runserver