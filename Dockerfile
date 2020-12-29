FROM ubuntu:18.04
COPY . /app
RUN Make /app
CMD python /HttpServiceApp/source/main.py