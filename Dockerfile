FROM python:3.9

RUN pip install --upgrade pip 

RUN  mkdir /app

ADD . /app

WORKDIR /app

RUN pip install -r requeriments.txt

CMD python /app/BoturuBot.py