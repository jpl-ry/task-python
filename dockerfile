FROM python:latest

RUN useradd -m jaipal
USER jaipal

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# 👇 This must include the templates folder
COPY . .

ENV PYTHONUNBUFFERED=1
EXPOSE 5000

CMD ["python", "main.py"]
