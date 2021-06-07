FROM python:3.8-slim

ENV HOME =  /usr/app
WORKDIR ${HOME}
COPY . ${HOME}
RUN pip install -r requirements.txt

CMD ["python3", "/usr/app/common_producer.py"]