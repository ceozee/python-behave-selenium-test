# python-behave-test-jupiter

Web Test automation using python behave and selenium for Jupiter

## Pre requisites

- Python 3.9.0
- python pip
- For windows users: Git bash for windows
- Webdrivers are installed. Please see: https://selenium-python.readthedocs.io/installation.html

## Setup

if user is using windows, best to use git bash for windows. cmd or powershell should also work
1. Go to desired folder (same folder level as your project folder)
2. Do: python -m venv ./venv
3. Do source venv/Script/activate. Make sure that you are in venv by checking. do: which python - it should be in the new path or you can see (venv) on cmd/terminal
4. Clone this repository
5. Go to python-behave-test-jupiter folder
6. Install requirements.txt by doing pip install -r requirements.txt
7. Run behave

## Run behave

when running behave, you can choose either of the following:
- behave
    - this will run all the test suites with no report. Result will be visible in terminal /cmd
- behave -f html -o <report_output.html>
    - this will use the html formatter and will create html file for the result
- behave features/feature_file.feature
    - this will run specific feature file. -f can be added as argument for reports


## Configurable browser
when using different browser, please change behave.ini executable path to where your browser driver is located. Then set env for the browser to use