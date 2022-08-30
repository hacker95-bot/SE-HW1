## Build SE-HW1 from source

Prerequisites

* [Python](https://www.python.org)
* [six](https://pypi.org/project/six/)

Optionally

* [pytest](https://pypi.org/project/pytest/)

Installing the dependencies:

python -m pip install --upgrade pip;

pip install flake8 pytest;

if [ -f requirements.txt ]; then pip install -r requirements.txt; fi;

After having all the dependencies:
```
# To clone the project from the repository:
git clone git@github.com:hacker95-bot/SE-HW1.git
```

To compile / install:
```bash
cd SE-HW1/code/
```

To run the tests
```bash
# Output is printed on the terminal
python __init__.py
```

