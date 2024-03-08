# Use the official Python image as the base image
FROM python:3.12

# Set a build argument for the Git commit hash
ARG COMMIT_HASH=unknown

# Label the Docker image with the Git revision
LABEL org.opencontainers.image.revision=$COMMIT_HASH

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Run collectstatic to gather static files
RUN python manage.py collectstatic --noinput

# Expose the port that the app will run on
EXPOSE 8000

# Command to run the application
CMD ["/usr/local/bin/gunicorn", "amicci_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
