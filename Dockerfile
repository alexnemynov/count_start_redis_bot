# Simple build
FROM python:3.12.3-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache -r /app/requirements.txt
COPY count_start_redis_bot /app/count_start_redis_bot
CMD ["python", "-m", "count_start_redis_bot"]