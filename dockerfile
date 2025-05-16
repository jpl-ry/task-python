FROM python:latest

RUN useradd -m jaipal

USER jaipal

WORKDIR /app

#RUN pip install --upgrade pip setuptools==65.5.0 wheel extension-helpers numpy jinja2

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 5000

CMD ["python", "main.py"]
