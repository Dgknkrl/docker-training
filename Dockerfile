# syntax=docker/dockerfile:1.4
FROM alpine
COPY --link /foo /bar
