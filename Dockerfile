FROM alpine:latest

EXPOSE 5000
WORKDIR /app
CMD nginx -c /nginx.conf

RUN apk add --no-cache nginx
ADD nginx.conf /

ONBUILD ADD . ./
