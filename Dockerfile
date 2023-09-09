FROM python:3.10-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "streamlit_app.py", "--server.port", "8080", "--server.host", "0.0.0.0"]
