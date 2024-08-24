# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

COPY ./devops/nginx/nginx.conf /etc/nginx/conf.d/myapp.conf

# Run gunicorn when the container launches
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
