FROM python:3.8.2
COPY www /www
WORKDIR /www
RUN pip install -r requirements.txt
COPY . /
WORKDIR /cdiscount
RUN pip install ./
WORKDIR /www
CMD ["flask","run", "--host=0.0.0.0", "--port=5000"]
