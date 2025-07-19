FROM python:3.11-slim-bullseye
WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/tokonoko12/thisis.git .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 10000
CMD ["uvicorn", "run:main_app", "--host", "0.0.0.0", "--port", "10000", "--workers", "4"]

