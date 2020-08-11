[![Build Status](https://travis-ci.com/huxaiphaer/huxy_travels_2.svg?branch=master)](https://travis-ci.com/huxaiphaer/huxy_travels_2)
[![codecov](https://codecov.io/gh/huxaiphaer/huxy_travels_2/branch/master/graph/badge.svg)](https://codecov.io/gh/huxaiphaer/huxy_travels_2)
# Huxy Travels

The number one stop experience for having fascinating tours, try us today.

### Requirements for setting up the project.
1. Python3. 
2. Django
3. Virtualenv. 
4. Redis. 
You need to install redis on your machine, then afterwards you activate it.
This is the command you run on mac ``` brew services start redis```
5. Celery. This is also needed to perform some background processes, for this project, 
celery is already in the `requirements.txt` file.
6. Postgres DB


### Installation on Mac

1 . First clone this repository 

```
$ https://github.com/huxaiphaer/huxy_travels_2.git
```

2 . Add the following variables in your Environment Variables permanently:

```buildoutcfg
CELERY_BROKER_URL=redis://localhost:6379/0
DB_NAME=huxy_tours
DEBUG_CONFIG=false
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
SECRET_KEY=any_secret_key
DB_PORT=port_number_for_db
DB_TEST=test_db_name
WEATHER_BASE_URL=api.openweathermap.org/data/2.5/forecast
WEATHER_API_KEY=1d4ce67223a53a013fc03ead36137396
CITIES_URL=https://raw.githubusercontent.com/huxaiphaer/travel_huxy/master/app/static/data/current_city_list.json
```

After, setting up the environment variables add create a Postgres Database called `huxy_tours`, followed by running  migrations with the commands 
below to create all the necessary tables :


**NOTE :**
- The commands below won't run unless  you have your Redis server running and as well
as setting all the environment variables above.

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py migrate --run-syncdb

```


3 . Then, create a virtual environment and install in on Mac :

```buildoutcfg
$ virtualenv env
$ source env/bin/activate
```

4.  After activating the `virtualenv`, then install the necessary dependencies :

```buildoutcfg
$ pip3 install -r requirements.txt
```

5. Activate celery to perform background tasks, open a new tab in the project directory.
Run this first command :

`$ celery -A huxy_travels_2 worker -l info`

Then, after running the above command, create another tab in the terminal with the environment variables and run
the command below :

`$ celery -A huxy_travels_2 beat -l info`


**HINT**:

_In order to run the commands smooth in different terminals ensure that the environment
variables a permanently saved._


6. After, that, open another terminal and now run the entire project with the following command:

  `$ python manage.py runserver`

Then, Viola you easily navigate to the server URL 
`http://120.0.0.1:8000` or `http://localhost:8000`


## Running with Docker.

The alternative way of running this project is by using Docker.

#### Requirements.

- Ensure that you have installed docker on your machine and you've started it.

After, installing , then run the following command in the root folder of the 
project to spin the container.

```python3

 $ docker-compose up --build

```

If the command is successfully done , it shows the `celery` logs 
of the beats.

To access, the application use `http://0.0.0.0:5005` (Ensure that all containers or services are up and running)

 #### Endpoints to create a user account and login into the application

| HTTP Method   | End Point             | Action          |
| ------------- | --------------------- |-----------------|
| POST          | /api/v1/auth/create   |Create an account|
| POST          | /api/v1/login         |Login user       |



#### Other Endpoints.

| HTTP Method   | End Point                                                   | Action                         |
| ------------- | ----------------------------------------------------------- |--------------------------------|
| POST          | /api/v1/tour                                                |Creates tour packages.          |
| GET           | /api/v1/tour                                                |Get list of tour packages.      |
| GET           | /api/v1/tour/<tour_id>                                      |Get tour package by ID.         |
| GET           | /api/v1/tourpackages/filter?first_date={f_d}&last_date={l_d}|Get tourpackages by date        |
| PUT           | /api/v1/tour/<tour_id>                                      |Update tour package by ID.      | 
| DELETE        | api/v1/tour/<tour_id>                                       |Delete tour package by ID       |
| PUT           | /api/v1/tour/booking/<tour_id>                              |Make a booking request          |
| DELETE        | /api/v1/tour/booking/<tour_id>                              |Delete a booking request        |
| GET           | /api/v1/weather_forecast/search/{lat}/{lon}                 |Get weather updates by location |
|               |                                                             |                                |


### Further More API Docs.

This is the [link](https://huxytours.docs.apiary.io/) to the API Docs.


### Running Tests Locally

Running tests of the project :

```python3
$ nosetests
```

Running tests with coverage :

```python3
$ nosetests --with-coverage
```


### Improvements
 Due to time being as a factor the following were left out, but they could improve on the 
 experience :
 
 - _Exhausting more on unit tests_.
 - _Hosting the project (e.g Heroku) etc._

### Contributors 

* [Lutaaya Idris](https://github.com/huxaiphaer)
