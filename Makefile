# https://paiml.com/docs/home/books/testing-in-python/chapter01-configuring-the-environment/

setup:
    python3 -m venv env

install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt