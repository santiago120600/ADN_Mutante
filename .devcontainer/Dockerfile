FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# COPY requirements.txt ./
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

CMD [ "python", "src/main.py" ]