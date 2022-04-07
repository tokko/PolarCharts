from python:alpine3.15

run mkdir /app
workdir /app
copy graphs.py /app/graphs.py
cmd python graphs.py /data/*
