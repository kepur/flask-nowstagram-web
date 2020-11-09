FROM python:3.7-stretch
WORKDIR /opt
COPY flask-nowstragram-web/requirements.txt /opt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
COPY flask-nowstragram-web/ /opt
CMD [ "python","runserver.py" ]
EXPOSE 7781