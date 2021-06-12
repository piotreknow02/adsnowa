FROM alpine:latest

RUN apk add --update nodejs npm
RUN mkdir /home/adsnowa
WORKDIR /home/adsnowa
ADD . /home/adsnowa
RUN npm install
CMD ["sh", "-c", "npm run dev"]
# docker build -t adsnowa .
# docker run -p 3000:3000 adsnowa 