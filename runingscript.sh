#!/bin/bash
python3 -m venv myenv
source myenv/bin/activate
pip install flask
python3 app.py