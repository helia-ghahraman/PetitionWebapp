# PetitionWebapp

## Overview

Welcome to the Web Programming project inspired by Karzar.ir. In this project, we've replicated the core features of Karzar.ir, offering users the ability to create, explore, and support campaigns. This project was a challenging endeavor, but we've done our best to bring the key functionalities to life.

## Features

### Users

- **User Registration and Login**: Create an account and log in to access the platform.
- **User Profile Management**: Edit and update your user profile information.
- **Campaign Creation**: Users can create campaigns with various details.
- **View Campaigns**:
  - Latest Campaigns: See the most recently added campaigns.
  - Most Popular Campaigns: Discover the campaigns with the highest popularity.
  - Successful Campaigns: View campaigns that have garnered a certain number of supporters.
  - Open Campaigns: Explore campaigns that are currently open for support.
- **Campaign Search**: Easily find campaigns based on criteria like title, date, success status, and more.
- **Support Campaigns**: Users can support open campaigns using national and contact numbers.

### Admin

- **Campaign Category Management**: Admins can oversee campaign categories.
- **User Management**:
  - User Approval and Disapproval: Admins can approve or disapprove user registrations.
  - User Profile Editing: Admins have the ability to edit user profiles.
- **View Campaigns**:
  - Latest Campaigns: Admins can see the most recently added campaigns.
  - Most Popular Campaigns: Discover the campaigns with the highest popularity.
  - Successful Campaigns: View campaigns that have garnered a certain number of supporters.
  - Open Campaigns: Explore campaigns that are currently open for support.
- **Campaign Search**: Admins can search among campaigns based on criteria like title, date, and time.

## Installation

To run the project, you'll need to follow these steps:

### Project Setup

1. **Clone Project**: Start by cloning the project to your local machine.

### Setting up the Virtual Environment

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv venv
   venv/Scripts/activate

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt

### Database Configuration

1. **Migrate Data to Database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

2. **Create Superuser**:
   ```bash
   python manage.py createsuperuser

3. **Collect Static Files**:
   ```bash
   python manage.py collectstatic

### Run the Server
**Start the Development Server**:

  ```bash
  python manage.py runserver
  ```

Now you're ready to explore and use the project.
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
