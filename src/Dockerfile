# Use the official Python image as a base
FROM python:3.10.0-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Set the environment variable to indicate that we are in production mode
ENV PYTHONUNBUFFERED 1

# Expose the port that Django will run on
EXPOSE 8000

# Run the Django development server (you can use Gunicorn for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
