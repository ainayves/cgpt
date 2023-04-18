FROM python:3.8-slim
RUN useradd --create-home --shell /bin/bash app_user
LABEL MAINTAINER="https://github.com/ainayves/cgpt"
WORKDIR /cgpt/
COPY requirements.txt ./
COPY . /cgpt
RUN pip install --no-cache-dir -r requirements.txt
USER app_user
COPY . .
CMD ["bash"]


