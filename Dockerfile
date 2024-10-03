# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the .env file into the container
COPY .env /app/.env

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Environment variable for the port
ENV PORT=8080

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the application using gunicorn for production
RUN pip install gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]