FROM python:3.8-slim
WORKDIR /mulit_thread_app
COPY . /mulit_thread_app
COPY app/ /mulit_thread_app/app

CMD ["python", "app/main.py"]