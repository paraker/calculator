# calculator
Just a super small repo to test CI with circleci

# pipenv
To download required packages from pypi, run this:

    pipenv --install
    
# pytest
Run module pytest with coverage flag on the testable code in the current directory
IMPORTANT to run pytest as a module to get the import statements correct!

    python -m pytest --cov .

# flake8
 
    flake8 --statistics