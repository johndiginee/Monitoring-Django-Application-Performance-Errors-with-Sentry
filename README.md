# Monitoring Django Application Performance Errors with Sentry

Sentry is an application monitoring platform that allows developers to track errors and performance data.

I added Sentry to my Django application so that I can track and resolve any errors or performance issues that occur while my application is in production.

### Installation Steps

1. Clone the repository:

        git clone https://github.com/johndiginee/Monitoring-Django-Application-Performance-Errors-with-Sentry.git


2. Change into the parent directory:

        cd Monitoring-Django-Application-Performance-Errors-with-Sentry


3. Set up a virtual environment:

        python3 -m venv venv


4. Activate your virtual environment:

        source venv/bin/activate


5. Install the Python dependencies:

        pip install -r requirements.txt


6. Create a .env file and set necessary secret keys below:


7. Apply migrations to create the database schema:

        python3 manage.py makemigratiions
        python3 manage.py migrate


8. Start the development server: 
 ```
 python3 manage.py runserver
 ```

## Screenshots
<img src="https://res.cloudinary.com/dkezlmzn1/image/upload/v1699615896/Screenshot_2023-11-10_at_11.36.50_AM_yochwv.png"/>
<img src="https://res.cloudinary.com/dkezlmzn1/image/upload/v1699615895/Screenshot_2023-11-10_at_12.10.49_PM_nlluot.png"/>
<img src="https://res.cloudinary.com/dkezlmzn1/image/upload/v1699617014/Screenshot_2023-11-10_at_12.42.40_PM_pyqvvd.png"/>