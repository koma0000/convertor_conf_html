FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
WORKDIR /
COPY . /
RUN apt-get update
RUN apt-get install nano
RUN pip3 install Flask-Cors
CMD ["python3", "conventor_config.py"]
