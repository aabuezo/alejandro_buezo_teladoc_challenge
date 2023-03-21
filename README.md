# Set up

You will need to install the following:

- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)

Or, in a terminal, from the base directory:

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
