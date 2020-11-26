FROM python:3.8

#ADD ./src /code

EXPOSE 5000

WORKDIR /flask1

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY ./ ./

CMD [ "python3", "./server.py" ]
