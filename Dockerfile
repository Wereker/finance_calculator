FROM python:3.13-slim

WORKDIR /app

COPY finance_calculator.py .
COPY r.txt .

RUN pip install -r r.txt

CMD ["python", "finance_calculator.py"]