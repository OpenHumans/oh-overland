release: python manage.py migrate
web: gunicorn oh_template.wsgi --log-file=-
worker: celery -A oh_template worker --concurrency 1
