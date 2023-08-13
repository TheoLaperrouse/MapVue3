FROM node:14 as build-stage

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

CMD ["npm", "run", "start"]
