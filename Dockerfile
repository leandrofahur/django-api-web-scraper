# # Use the official Python image from the Docker Hub
# FROM python:3.11

# # Set environment variables for Django
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Set the working directory in the container
# WORKDIR /usr/src/app

# # Copy the requirements file to the container
# COPY requirements.txt ./

# # Install any dependencies from the requirements file
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the current directory contents into the container at /usr/src/app
# COPY . .

# # Expose the port the app runs on
# EXPOSE 8000

# # Run Django and start the development server
# CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]