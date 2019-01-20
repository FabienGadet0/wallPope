FROM heroku/miniconda

ADD ./requirements.txt /tmp/requirements.txt
ADD ./conda-requirements.txt /tmp/conda-requirements.txt

RUN pip install -qr /tmp/requirements.txt

ADD ./srcs /opt/webapp/
WORKDIR /opt/webapp

RUN conda install --file /tmp/conda-requirements.txt

CMD gunicorn --bind 0.0.0.0:$PORT wsgi