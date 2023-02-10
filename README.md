# PetitionWebapp

## installation and start:
clone project.

## create and activate virtualenv:
python -m venv venv

venv/Scripts/activate

## install requirements.txt:
pip install -r requirements.txt

## migrating the data to database:
python manage.py makemigrations

python manage.py migrate

## create superuser:
python manage.py createsuperuser

## collect statics
python manage.py collectstatic

## run server:
python manage.py runserver