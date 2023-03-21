# UI Homework Assignment

## Story
As an Engr. I need to automate: https://www.way2automation.com/angularjs-protractor/webtables/

### Scenario 1
Add a user and validate the user has been added to the table

### Scenario 2
Delete the user "novak" from the table and validate the user has been deleted.

## Set up

You will need to install the following in order to run the tests:

- Python 3.10 or above
- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)

Clone this repo: 
```bash
git clone https://github.com/aabuezo/alejandro_buezo_teladoc_challenge.git
```

In a terminal, from the base directory:

1. Create the virtual environment
```bash
python -m venv venv
```
2. Activate it
```bash
source venv/bin/activate
```
3. Install requirements.txt
```bash
pip install -r requirements.txt
```

## Running the tests

To run the tests, you'll need to do this in a terminal, in the base directory:
1. Linux
```bash
source venv/bin/activate
python -m behave
```
2. Windows
```bash
cd venv\Scripts
.\activate
python -m behave
```

If you want to run the tests in PyCharm, you'll need to create appropriate configurations.
