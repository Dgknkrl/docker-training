# syntax=docker/dockerfile:1.4
FROM nginx
COPY index.html /usr/share/nginx/html/index.html
