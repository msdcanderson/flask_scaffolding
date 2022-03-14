# flask_scaffolding
Scaffolding application

<p>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://badgen.net/badge/code%20style/black/000"></a>
</p>

## Getting Started

### Running the app locally

First create a virtual environment with conda or venv inside a temp folder, then activate it.

```
virtualenv venv

# Windows
venv\Scripts\activate
# Or Linux
source venv/bin/activate

```

Clone the git repo, then install the requirements with pip

```

git clone https://github.com/msdcanderson/flask_scaffolding.git
cd flask_scaffolding
pip install -r requirements.txt

```

Run the app

```

python app.py

```

## Freeze Requirements

When you add a library, remember to freeze the requirements.txt

`pip freeze > requirements.txt`


## Working with Issues

When an issue is completed please: 

- leave a useful comment
- leave the issue 'Open' (I will close the issue once it has been tested)
- assign the issue to me

## Committing to repo

When you make a commit please:

- put the issue number you are working on in the commit message
- a short useful description

## Running app

https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/

```cmd
set FLASK_APP=flask_scaffolding
set FLASK_ENV=development
flask run
```

```powershell
$env:FLASK_APP = "flask_scaffolding"
$env:FLASK_ENV = "development"
flask run
```

```bash
export FLASK_APP="flask_scaffolding"
export FLASK_ENV="development"
flask run
```

## Integrating Dash into Flask

[Source](https://hackersandslackers.com/plotly-dash-with-flask/)