FROM acencini/rpi-python-serial-wiringpi:latest

RUN pip install -U RPi.GPIO paho-mqtt

RUN mkdir /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app

CMD python relay_controller.py