# docker build -t myimage .
# docker run -d --name mycontainer -p 80:80 myimage


FROM python:3.7.6-buster

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY ./recommenderSystem /code/recommenderSystem

CMD ["uvicorn", "recommenderSystem.main:app","--host", "0.0.0.0", "--port", "80"]