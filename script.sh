#!/bin/bash
rm graphs/*
mkdir data5
sudo cp ~/host/data5/data5.zip data5
unzip data5/data5.zip data5
rm data5/*.zip
./graphs.py data5/*
zip graphs.zip graphs/*
sudo mv graphs.zip ~/host
