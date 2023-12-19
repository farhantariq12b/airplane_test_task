# Airplane Test Task

This Django project implements a RESTful API for managing information about 10 different airplanes. Each airplane is characterized by its fuel tank capacity, fuel consumption per minute, and the impact of passengers on fuel consumption.

## Requirements

To run this project, you will need the following:

- Python 3.x

## Setup Instructions

1. Clone the repository
```shell
git clone git@github.com:farhantariq12b/airplane_test_task.git
```

2. Create a virtual environment (recommended but optional):
```shell
python -m venv venv
```

3. Install the required Python packages:
```shell
pip install -r requirements.txt
```

4. Run the Django migrations:
```shell
python manage.py migrate
```


## Usage

To start the Django development server, run the following command:
```shell
python manage.py runserver
```

The API will be accessible at http://127.0.0.1:8000/api/airplanes/.

You can use any api endpoint testing tool i.e. Postman by sending post request on above endpoint having request body formant as below: -
```
[
    {"id": 1, "passenger_assumptions": 50},
    {"id": 2, "passenger_assumptions": 40},
    {"id": 3, "passenger_assumptions": 30},
] 
```

## Running Tests

- To run tests and check coverage, use the following commands:

```shell
python3 -m coverage run manage.py test
coverage report
```

## Project Structure
The project directory structure is as follows:

1. Airplane_project: Django app containing Django app settings, urls of project.
2. Airplanes/: Django app containing tests, urls, models, serializers and views where actual functionality is implemented.


## File Structure
airplanes/views.py: Implementation of the API views.
airplanes/tests/: Test files for the application.
airplanes/models.py: Definition of the Airplane model.
requirements.txt: List of Python dependencies.
