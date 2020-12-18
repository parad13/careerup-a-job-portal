release: python manage.py migrate 
         pip freeze > requirements.txt

web: gunicorn CareerRide.wsgi --log-file -
