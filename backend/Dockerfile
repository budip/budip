# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the backend code to the container
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
