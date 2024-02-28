# Use a base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Change to the src directory
RUN cd src/

# Install dependencies using Poetry
RUN poetry install

# Set the environment variable for the API key
ENV OPENAI_API_KEY=""

# Command to run the application
CMD ["poetry", "run", "cgpt"]
