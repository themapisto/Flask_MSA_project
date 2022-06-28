FROM python:3.9
ENV PYTHONBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install -r jinja2<3.1.0
COPY . /app
# dockerfile
CMD python main.py