release: python manage.py migrate
web: daphne project.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=project.settings.prod -v2