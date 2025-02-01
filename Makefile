
test:
	python manage.py test


lint:
	flake8


format:
	black .


check:
	python manage.py test
	flake8


run:
	python manage.py runserver