FROM python:3.12-slim

# Upgrade pip and install security updates
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends gcc && \
	pip install --upgrade pip && \
	apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir /simpleapi
COPY simpleapi ./simpleapi
WORKDIR /simpleapi
RUN pip install poetry  
RUN poetry install  
EXPOSE 8000

CMD ["poetry", "run", "fastapi", "dev", "simpleapi", "--host", "0.0.0.0", "--port", "8000"]