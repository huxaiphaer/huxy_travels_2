#Run migrations
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

# Run Celery worker
celery -A huxy_travels_2 worker -l info &

# Run Celery beat
celery -A huxy_travels_2 beat -l info &

python manage.py runserver 0.0.0.0:5005