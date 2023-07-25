FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WARKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["pythohn3", "app.py"]