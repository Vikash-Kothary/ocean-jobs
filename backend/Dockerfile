# File: ocean-jobs-backend
# Author: Vikash Kothary <kothary.vikash@gmail.com>
# Version: v0.0.0

FROM python:3.7 as base
#RUN apt-get install python libxml2 zlib1g

ENV PYTHONPATH=src
ENV PYTHONUSERBASE=/mnt/vendor


# /install
FROM base as install

RUN mkdir /install
WORKDIR /install

COPY requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

# /app
FROM base

COPY --from=install /install /app
COPY . install/app

EXPOSE 5000

CMD ["python", "main.py"] 