FROM python:2

WORKDIR /src

# install the deps first, creates a nice snapshot
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

COPY src /src

CMD [ "celery", "worker", "--app", "worker", "--loglevel=INFO", "--concurrency=8" ]
