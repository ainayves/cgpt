# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

LABEL MAINTAINER="https://github.com/ainayves/cgpt"

# Set the working directory to /app
WORKDIR /cgpt/

# Copy the current directory contents into the container at /app
COPY . /cgpt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN python setup.py develop
RUN python setup.py sdist bdist_wheel
ENTRYPOINT [ "cgpt.sh" ]
