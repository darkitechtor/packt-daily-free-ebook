FROM python:3.7-slim-buster

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        apt-utils \
        build-essential \
        libffi-dev \
        libpq-dev \
        libssl-dev \
        python3-pandas \
        python3-numpy

ENV PYTHONPATH="${PYTHONPATH}:/usr/lib/python3/dist-packages"

RUN pip install -U pip setuptools wheel \
	&& pip install pyOpenSSL \
    && pip install apache-airflow[crypto,postgres] \
	&& pip install pyppeteer

# Pyppeteer
RUN apt-get update \
    && apt-get install -y chromium \
    && apt-get install -y ca-certificates \
        fonts-liberation \
        libappindicator3-1 \
        libasound2 \
        libatk-bridge2.0-0 \
        libatk1.0-0 \
        libc6 \
        libcairo2 \
        libcups2 \
        libdbus-1-3 \
        libexpat1 \
        libfontconfig1 \
        libgbm1 \
        libgcc1 \
        libglib2.0-0 \
        libgtk-3-0 \
        libnspr4 \
        libnss3 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        libstdc++6 \
        libx11-6 \
        libx11-xcb1 \
        libxcb1 \
        libxcomposite1 \
        libxcursor1 \
        libxdamage1 \
        libxext6 \
        libxfixes3 \
        libxi6 \
        libxrandr2 \
        libxrender1 \
        libxss1 \
        libxtst6 \
        lsb-release \
        wget \
        xdg-utils

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true
ENV PUPPETEER_EXECUTABLE_PATH /usr/bin/chromium

COPY ./entrypoint.sh /entrypoint.sh

EXPOSE 8080

ENV AIRFLOW_HOME=/app/airflow
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
ENV AIRFLOW__CORE__LOAD_DEFAULT_CONNECTIONS=False
ENV AIRFLOW__CORE__FERNET_KEY=<your secret key>
ENV AIRFLOW__WEBSERVER__EXPOSE_CONFIG=True

ENTRYPOINT [ "/entrypoint.sh" ]
