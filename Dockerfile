FROM python:3.9
WORKDIR /usr/src/app
RUN apt-get -y update
RUN apt-get -y upgrade

COPY . .

RUN pip install --no-cache-dir --upgrade pip

RUN pip --default-timeout=1000 install --extra-index-url=https://download.pytorch.org/whl/cu117 torch==2.0.1+cu117

RUN pip --default-timeout=1000 install --no-cache-dir -r requirements.txt

EXPOSE 3040
CMD ["python3", "./manage.py"]