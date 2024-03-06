FROM python:3

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip

COPY /api/requirements.txt .

RUN pip install -r requirements.txt

COPY /api .

