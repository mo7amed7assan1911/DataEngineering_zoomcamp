FROM python

WORKDIR  /app

COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]


ENTRYPOINT ["streamlit", "run", "./code/app.py"]