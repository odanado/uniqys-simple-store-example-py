FROM python:3.7

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY src/main.py /app/src/main.py

EXPOSE 56080

CMD python src/main.py
