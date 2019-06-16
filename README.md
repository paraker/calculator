# calculator
Just a super small repo to test CI with circleci

# pipenv
If required, install pipenv on your system

    pip3 install pipenv

Activate the virtual environment

    . $(pipenv --venv)/bin/activate
    
Donwload required packages from pypi

    pipenv install
    
# pytest
Run module pytest with coverage flag on the testable code in the current directory
IMPORTANT to run pytest as a module to get the import statements correct!

    python -m pytest --cov .

# flake8
 Run a PEP8 test on your app code
 
    flake8 app/*.py --statistics