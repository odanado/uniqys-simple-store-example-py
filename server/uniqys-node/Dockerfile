FROM node:10.9.0

ENV LEVELDOWN_DIR /data/.leveldown
RUN mkdir -p ${LEVELDOWN_DIR}
VOLUME ${LEVELDOWN_DIR}

EXPOSE 8080
EXPOSE 56010
EXPOSE 56011

WORKDIR /app

COPY ./package.json /app/package.json
COPY ./yarn.lock /app/yarn.lock

RUN yarn

COPY index.ts /app/index.ts
COPY tsconfig.json /app/tsconfig.json

CMD yarn dev
