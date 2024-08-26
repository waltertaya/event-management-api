.PHONY
run:
	python3 manage.py runserver

.PHONY
migrate:
	python3 manage.py migrate

.PHONY
makemigrations:
	python3 manage.py makemigrations

.PHONY
shell:
	python3 manage.py shell

.PHONY
createsuperuser:
	python3 manage.py createsuperuser

.PHONY
test:
	python3 manage.py test

.PHONY
collectstatic:
	python3 manage.py collectstatic

.PHONY
install:
	pip3 install -r requirements.txt

.PHONY
clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "__pycache__" -exec rm -rf {} \;
	rm -rf staticfiles
	rm -rf mediafiles
	rm -rf db.sqlite3
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf .mypy_cache
