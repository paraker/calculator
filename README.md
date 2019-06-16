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

# TODO
### peer review, realpython advanced git tips
https://realpython.com/advanced-git-for-pythonistas/
https://help.github.com/en/categories/collaborating-with-issues-and-pull-requests

###Artifacts and CI/CD
Would be useful to create a deployable artifact (finished, packaged product).
Haven't found a good resource for this just yet. 