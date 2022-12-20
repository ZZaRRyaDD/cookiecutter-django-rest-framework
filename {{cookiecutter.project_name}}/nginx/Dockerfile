FROM python:3.10.5-slim-bullseye as server

ARG APP_HOME=/server/

RUN apt-get update && \
    apt-get install --no-install-recommends -y libpq-dev build-essential

COPY ./server ${APP_HOME}

WORKDIR ${APP_HOME}

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

RUN python ./manage.py collectstatic --noinput

#########################################

FROM nginx:1.19.2

RUN rm -v /etc/nginx/nginx.conf
ADD ./nginx/nginx.conf /etc/nginx/

RUN mkdir /nginx
COPY --from=server /server/staticfiles /nginx/static
