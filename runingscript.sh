#!/bin/bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
pip install flask
python3 app.py