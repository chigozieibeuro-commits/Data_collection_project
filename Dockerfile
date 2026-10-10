FROM python:3.13

WORKDIR /app

Copy requirement.text .

Run pip install --no-cache-dir -r requirement

COPY . .

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]