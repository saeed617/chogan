FROM python:3.7

WORKDIR /chogan/

COPY    requirements.txt requirements.txt
RUN     pip install -r requirements.txt

COPY    . /chogan/

EXPOSE  8000
CMD     ["./docker-entrypoint.sh"]
