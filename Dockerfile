FROM quay.io/astronomer/astro-runtime:11.3.0-base

USER root
COPY packages.txt packages.txt

RUN apt-get update && \
    apt-get install -y $(cat packages.txt) && \
    apt-get clean 

COPY include/whl_files/apache_airflow_providers_common_io-1.4.0-py3-none-any.whl /tmp
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
USER astro