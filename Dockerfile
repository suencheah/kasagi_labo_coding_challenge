FROM python:3.10

WORKDIR /app

COPY Challenge_A.txt .
COPY Challenge_B.py .

RUN mkdir /output

CMD ["python", "Challenge_B.py"]