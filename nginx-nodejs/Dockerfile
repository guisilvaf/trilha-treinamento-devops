FROM nginx

LABEL version="1.0.0" description="Container Nginx e NodeJS" maintaner="Guilherme Silva <https://github.com/guisilvaf>"

WORKDIR /app

COPY ./start.sh /start.sh
COPY ./app /app

RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
RUN apt-get install -y nodejs
RUN npm install

ENV PORT=3000

EXPOSE 80

CMD [ "/start.sh" ]