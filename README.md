# SCRIPT GET N IMAGE EVERY 2 HOURS

## Set virtual environment
`python3 -m venv venv`
### Activate
`. venv/bin/activate`
### Install requirements
`pip install -r requirements.txt`

### Run rabbitmq
`sudo rabbitmq-server`

### Run script
1. Open another terminal
2. In that terminal:
    - set environment variables  
    `URL= unsplash api url`   
    `CLIENT_ID = Access Key from unsplash api`  
    `COUNT = number of image you want`  
    `QUERY = selection to photos matching such as dog, girl, cat ....`  
    `ORIENTATION = Filter by photo orientation. Optional. (Valid values: landscape, portrait, squarish)`  

    - RUN: `celery -A src.schedule worker -B -l INFO`  
