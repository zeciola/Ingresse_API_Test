# Use the Python3.7.3 image
FROM python:3.7.3-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install -r dev-requirements.txt

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]