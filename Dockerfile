FROM python:2.7
#FROM python

#CMD ['mkdir', '-p', '/opt/app']
RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY ./app/requirements.txt /opt/app/requirements.txt
RUN pip install -r /opt/app/requirements.txt

COPY ./app/ /opt/app/
#RUN pip install -e .
#EXPOSE 5000
# We could run all our tests here. How? :)
#CMD ["python","/opt/dockerflasktesting/FlaskHello/hello.py"]
