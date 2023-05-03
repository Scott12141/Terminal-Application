#!/bin/bash

python3 -m venv ta-venv
source ta-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py