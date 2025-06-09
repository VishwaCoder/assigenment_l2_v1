# Please follow the below steps to setup the Django web app on your local virtual environment.

1. Clone the git repo from here https://github.com/VishwaCoder/assigenment_l2_v1.git
2. Run cd assigenment_l2_v1/
3. Run python -m venv py_env to create virtual environment of python
4. Run py_env\Scripts\activate to activate the virtual env
5. Run pip install -r requirements.txt to install dependencies
6. Run cd pricing_module_l2
7. Run python manage.py makemigrations
8. Run python manage.py migrate
9. Run python manage.py createsuperuser (provide username, emial and password; use the same credentials to login to Django Admin Panel later)
10. Run python manage.py runserver (start Django web server default at (http://127.0.0.1:8000/) - to view the actual ui navigate to http://127.0.0.1:8000/app/home/)

# Notes -:

1. New pricing configuration entry can be created by logging into Django Admin panel. (http://127.0.0.1:8000/admin/prc_mdl_app/price/)
2. While creating new entries for configurations make sure valid email is provided for field "Created by" for further reference; whereas rest of the fields are integer (except update by and update at, these values will be automatically updated when any configuration is updated.)
3. Please refer to (http://127.0.0.1:8000/app/home/) after starting the app for evaluating core functionality.
4. This page (app/home/) depicts the table of added pricing configuration and editable custom fields to update particular configuration and associated actions on it such as, update, enable/disable config and delete.
5. Moreover, when any field(s) is/are updated by user, the Updated By and Updated At gets updated automatically as part of audit logs.
6. Please make sure at any instance of time only one configuration must be active (Enabled), and rest of the configurations should be disabled (by default is Disabled). To calculate the final price, this active configuration will be used automatically in backend.
7. Once one or more entries of configuration are added and a particular configuration is set as Enabled, navigate to (http://127.0.0.1:8000/app/price-calculator/).
8. This page (app/price-calculator/) holds  two input fields to accept time duration and traveled distance to calculate final invoice price. This is an API exposed from the backend to evaluate the price.

# Regret for -:
1. Could not able to add data validations for form fields.
2. No flash messages for errors/success.
3. No unit tests for backend functionality.
4. And anything else that has been missed.

- I have tried to implement most of the core features as mentioned in the problem statement with best of my knowledge and understanding. Due to some critical work conditions I didn't get enough time to incorporate above missing things. I would like to hear from you if I missed anything or I might have analyzed requirements incorrectly so that I can rectify the mistakes and make it little more better. Thanks for this wonderful opportunity, looking forward for your positive response ! :) 
