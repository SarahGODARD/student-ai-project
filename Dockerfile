FROM tensorflow/tensorflow:2.0.0a0-py3

WORKDIR /app

EXPOSE 8000

# The code to run when container is started:
# COPY ./ .

RUN apt-get update && apt-get -y install libglib2.0-0 libsm6 libxext6 libxrender-dev

ADD requirements.txt .
RUN pip install -r requirements.txt
COPY ./ .
CMD gunicorn -b 0.0.0.0:$PORT -t 600 src.wsgi:application --log-file -
