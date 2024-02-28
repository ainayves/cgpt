FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN cd src/
RUN poetry install
ENV OPENAI_API_KEY=""
CMD ["poetry", "run", "cgpt"]
