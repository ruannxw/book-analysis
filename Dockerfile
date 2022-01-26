FROM python:3.8

WORKDIR /code
ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
EXPOSE 5000
COPY . .

CMD ["gunicorn","-c","gunicorn.conf.py","wsgi:app"]