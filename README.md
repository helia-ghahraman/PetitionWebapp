# PetitionWebapp

## installation and start:
clone project.

## create and activate virtualenv:
python -m venv venv
venv/Scripts/activate

## install requirements.txt:
pip install -r requirements.txt

## migrating the data to database:
manage.py makemigrations
manage.py migrate

## create superuser:
manage.py createsuperuser

## run server:
manage.py runserver
