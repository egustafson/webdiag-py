FROM python:3-slim
RUN apt update && apt upgrade -y
RUN apt install -y net-tools
WORKDIR /app
COPY requirements.txt .
COPY pyproject.toml .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH=/app
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
