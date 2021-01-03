#!/bin/bash

source `pwd`/venv/bin/activate

if [ $? -eq 0 ]; then
	#google-chrome --incognito http://localhost:5000/download
	python -u download.py
else
	echo -e "App NOT up. Check logs."

fi
