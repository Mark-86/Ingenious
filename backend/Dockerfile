FROM node:16-alpine3.15

WORKDIR /backend

COPY package.json . 

RUN npm install 

COPY . . 

RUN npm run build 

CMD ["node","start:prod"]