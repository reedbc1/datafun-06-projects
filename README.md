# datafun-06-projects
Brendan Reed
9/30/2023
github repo link: https://github.com/reedbc1/datafun-06-projects

## Description

These are a few guided data projects I did through the Intro to Data Analytics course at Northwest MO State University.

## Virtual environment instructions

open cmd (if using windows) and navigate to datafun-06-projects in your files using cd %path%.
example:
```shell
cd %path%
```

setting up virtual environment
```shell
python -m venv .venv
```

activate the virtual environemnt
```shell
.venv\Scripts\activate
```

after calling this command, the terminal will change to show that you are now in a virtual environment.

## Running scripts

after following the above, run a python script.
```shell
python scriptname.py
```

## Installing external dependencies

In the active virtual environment, install all dependencies from requirements.txt to the virtual environment.
```shell
python -m pip install --upgrade -r requirements.txt
```

## Step 5: Working with Notebooks

In the active virtual environment, create a Python kernel to run our notebooks. 

```shell
python -m ipykernel install --user --name .venv --display-name "Python (.venv)"
```