# Ink Inception Backend

Ink Inception is a web application backend built with Django. This backend powers the application's API, handles user authentication, data storage, and serves static and media content. This backend also integrates with external services like PostgreSQL, Redis, AWS S3, and Celery for task management.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
  - [Using EC2 and RDS](#using-ec2-and-rds)
  - [Setting up CI/CD with GitHub Actions](#setting-up-cicd-with-github-actions)
- [Contributing](#contributing)
- [License](#license)

## Features

- RESTful API built with Django and Django Rest Framework.
- JWT Authentication for secure user login and registration.
- Task management using Celery and Redis.
- Static and media file storage using AWS S3.
- CI/CD pipeline using GitHub Actions for deployment.
- Configurable via environment variables for different deployment environments.

## Technologies Used

- **Django:** The web framework used for building the backend.
- **Django Rest Framework:** For building the RESTful API.
- **PostgreSQL:** Database for storing application data.
- **Redis:** For caching and task queuing.
- **Celery:** Task queue for handling asynchronous tasks.
- **Gunicorn:** WSGI HTTP server for running the Django application.
- **Nginx:** Web server for serving static files and reverse proxying to Gunicorn.
- **Docker:** Containerization for local development.
- **AWS S3:** For storing static and media files.
- **AWS RDS:** Managed PostgreSQL database.

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- Redis
- AWS S3 account (optional for local development)
- Docker (optional for local development)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ink-inception-backend.git
    cd ink-inception-backend
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables as described in the [Environment Variables](#environment-variables) section.

### Running the Application

1. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

2. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

3. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

4. (Optional) Start Celery for background tasks:

    ```bash
    celery -A config worker --loglevel=info
    ```

5. (Optional) If you're using Docker, you can start the entire application stack using `docker-compose`:

    ```bash
    docker-compose up --build
    ```

## Environment Variables

Create a `.env` file in the root directory with the following content:

```env
SECRET_KEY=your-secret-key
PRODUCTION=True
DJANGO_CORS_ALLOW_ALL_ORIGINS=True

API_VERSION=1

# CELERY
CELERY_BROKER=redis://localhost:6379/0
CELERY_BACKEND=redis://localhost:6379/0
CELERY_TIMEZONE=UTC

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

DJANGO_POSTGRES_NAME=your-db-name
DJANGO_POSTGRES_USER=your-db-user
DJANGO_POSTGRES_PASSWORD=your-db-password
DJANGO_POSTGRES_HOST=your-db-host
DJANGO_POSTGRES_PORT=5432

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_USE_SSL=True
EMAIL_USE_TSL=False
EMAIL_HOST=smtp.example.com
EMAIL_PORT=465
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password

# S3
AWS_S3_STORAGE_BUCKET_NAME=your-s3-bucket-name
AWS_S3_ACCESS_KEY_ID=your-access-key-id
AWS_S3_SECRET_ACCESS_KEY=your-secret-access-key
AWS_S3_REGION_NAME=us-east-1
AWS_S3_ENDPOINT_URL=https://s3.amazonaws.com
```

## Deployment

### Using EC2 and RDS

1. **Set up an EC2 instance**  
   Launch an EC2 instance and configure it with the necessary software:
   - Python 3.10+
   - PostgreSQL client
   - Redis
   - Nginx

2. **Set up RDS for PostgreSQL**  
   - Create a PostgreSQL database instance on Amazon RDS.
   - Configure your application to use the RDS instance by updating the corresponding environment variables in your `.env` file:
     ```env
     DJANGO_POSTGRES_NAME=your-rds-db-name
     DJANGO_POSTGRES_USER=your-rds-db-user
     DJANGO_POSTGRES_PASSWORD=your-rds-db-password
     DJANGO_POSTGRES_HOST=your-rds-db-host
     DJANGO_POSTGRES_PORT=5432
     ```

3. **Use pm2 to manage Gunicorn**  
   Install `pm2` to run and manage your Gunicorn server on your EC2 instance:
   ```bash
   sudo npm install -g pm2
   pm2 start gunicorn --name ink-inception-backend -- gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
   pm2 startup
   pm2 save
   ```

4. **Set up Nginx as a reverse proxy**
   Configure Nginx to serve as a reverse proxy for Gunicorn:

   - Create an Nginx configuration file for your app.
   - Set up Nginx to forward requests from port 80 to Gunicorn running on port 8000.
   - Ensure that static and media files are correctly served by Nginx.

5. **Deploy code to EC2**
   - You can deploy your code to the EC2 instance using scp or by setting up a CI/CD pipeline with GitHub Actions (see the next section).

### Setting up CI/CD with GitHub Actions
1. **Create GitHub Secrets**
   Store your sensitive information like SSH key, EC2 IP, and environment variables as GitHub Secrets:

   - EC2_SSH_KEY
   - EC2_PUBLIC_IP
   - Other necessary environment variables

2. **Create a GitHub Actions workflow**
   Define a workflow (e.g., deploy.yml) that automates the deployment process. This includes:

   - Checking out your code
   - Installing dependencies
   - Copying files to your EC2 instance using scp
   - Running deployment scripts on your EC2 instance

### Contributing
If you'd like to contribute to this project, please open an issue or submit a pull request with your changes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
