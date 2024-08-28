.PHONY: run migrate makemigrations shell createsuperuser test collectstatic install clean

run:
    python3 manage.py runserver

migrate:
    python3 manage.py migrate

makemigrations:
    python3 manage.py makemigrations

shell:
    python3 manage.py shell

createsuperuser:
    python3 manage.py createsuperuser

test:
    python3 manage.py test

collectstatic:
    python3 manage.py collectstatic

install:
    pip3 install -r requirements.txt

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
