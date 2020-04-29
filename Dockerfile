FROM python:3.8.2
COPY www /www
WORKDIR /www
RUN pip install -r requirements.txt
COPY . /
WORKDIR /cdiscount
RUN pip install ./
WORKDIR /www
CMD ["python","app.py"]