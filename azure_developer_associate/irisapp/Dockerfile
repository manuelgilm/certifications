FROM python:3.11-slim 

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /irisapp
# Set the working directory
WORKDIR /irisapi
# Copy folders
COPY irisapi /irisapi
# install poetry 
RUN pip install poetry
# Install dependencies
RUN poetry install 
# Expose the port the app runs on
EXPOSE 8000
# Command to run the app
CMD ["poetry", "run", "fastapi","dev", "irisapi", "--host", "0.0.0.0", "--port", "8000"]



