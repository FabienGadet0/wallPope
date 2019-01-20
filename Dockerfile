#FROM heroku/miniconda
FROM continuumio/miniconda3

# ADD ./requirements.txt /tmp/requirements.txt
# ADD ./conda-requirements.txt /tmp/conda-requirements-linux.txt

# RUN pip install -qr /tmp/requirements.txt

ADD ./srcs /opt/webapp/
WORKDIR /opt/webapp

RUN conda install -c anaconda openssl beautifulsoup4
RUN conda install requests
RUN pip install basc_py4chan
# RUN conda install --file /tmp/conda-requirements-linux.txt

CMD ["python", "main.py"]