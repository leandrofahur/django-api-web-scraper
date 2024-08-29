# Base image from where the container will be built from
FROM python:3.11-slim

# Set the working directory where the commands will be executed relative to
WORKDIR /app

# Copy the requirements file to the working directory [source, destination]
COPY requirements.txt ./

# Run the command to install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the WORKDIR [/app] (This is very important, because it enables "hot-reloading")
COPY . .

# # Set environment variables for Django
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Expose the port the app runs on
# EXPOSE 8000

# # Run Django and start the development server
# CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]

