FROM python:3.13-slim

WORKDIR /app

COPY finance_calculator.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "finance_calculator.py"]