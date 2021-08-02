#!/bin/sh

# make sure python3, virtualenv is installed
python3 -m pip install -U virtualenv

# 1. create venv folder and swith to this evn
python3 -m virtualenv testenv

source testenv/bin/activate

# 2. install test framework
pip3 install pytest
pip3 install pytest-html
pip3 install pytest-cov

# 3. install requirements
pip install -r ../buildscript/requirements

# 4. run test
PYTHONPATH=..
export PYTHONPATH
pytest -s -v --capture=sys --show-capture=all --html=pytest-report.html --self-contained-html
test_result=$?

# 5. clean up
deactivate
rm -rf testenv

# 6. exit
exit $test_result