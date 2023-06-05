FROM python:3.11.3-bullseye

EXPOSE 8000

RUN mkdir -p /home/project

WORKDIR /home/project

COPY . .

RUN pip3 install pipenv

RUN pipenv install

ENTRYPOINT ["python3"] 

CMD ["app/manage.py", "runserver", "0.0.0.0:8000"]