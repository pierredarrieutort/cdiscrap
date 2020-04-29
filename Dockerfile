FROM python:3.8.2
ENV FLASK_APP "www/app.py"
COPY . /www
WORKDIR /www
RUN pip install -r www/requirements.txt
COPY . /
WORKDIR /
RUN pip install ./
WORKDIR /www
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["www/app.py"]
