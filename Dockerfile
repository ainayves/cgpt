# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

LABEL MAINTAINER="https://github.com/ainayves/cgpt"

# Set the working directory to /app
WORKDIR /cgpt/
# Copy the current directory contents into the container at /app
COPY . /cgpt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# create a shell script that will invoke the `cgpt()` function
RUN echo '#!/bin/sh\n cgpt "$@"' > /cgpt/cgpt.sh && \
    chmod +x /cgpt/cgpt.sh

RUN python setup.py develop
RUN python setup.py sdist bdist_wheel

# set the entrypoint to the shell script
ENTRYPOINT ["/cgpt/cgpt.sh"]


