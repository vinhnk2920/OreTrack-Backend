# Set the base image to Python 3.9
FROM python:3.10.9-slim-bullseye

# Set the working directory
WORKDIR /backend

# Copy the requirements file to the container
COPY . .

# Install the requirements
RUN pip install -r requirements.txt

# Expose the port that the application listens on
EXPOSE 5000

# Set the environment variable
ENV FLASK_APP=app.py

# Start the Flask application
CMD [ "flask", "run", "--host=0.0.0.0" ]
