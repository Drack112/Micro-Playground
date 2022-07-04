FROM python:3.9-bullseye

WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y \
    && apt install gcc python3-dev musl-dev bash build-essential libssl-dev libffi-dev gettext -y

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN sed -i 's/\r$//g' /home/app/entrypoint.sh
RUN chmod +x /home/app/entrypoint.sh

COPY . .

ENTRYPOINT ["/home/app/entrypoint.sh"]