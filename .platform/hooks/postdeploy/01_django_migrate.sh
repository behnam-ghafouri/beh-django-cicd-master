#!/bin/bash

source /var/app/venv/*/bin/activate && {
pip install -r  requirements.txt
# collect static
python manage.py collectstatic --noinput;
# log which migrations have already been applied
python manage.py showmigrations;
# migrate user model
python manage.py migrate users --noinput;
# migrate the rest
python manage.py migrate --noinput;
}