
# Project Description

This script generates a Dockerfile with the basic settings to deploy your flask application to heroku. And as a bonus a `steps.txt` with the step by step for you to publish the project.

## Installation from Pypi
`pip install sdf-heroku-deploy`

## Module Usage
**Run the script inside your project folder**
```python
from sdf_heroku_deploy import main
main()
```


## CLI Usage

### Get the list of available commands

`sdfh_cli --help`

Output 

```
Options:
  -img, --image_name TEXT       Type the name of the image you want to give   
                                the image to be created.
  -hap, --heroku_app_name TEXT  Type the name of the heroku app you want to   
                                give the app to be created.
  -r, --run TEXT                Type the name of the file that runs your flask
                                application.
  --help                        Show this message and exit.
```
##  Commands usage example

1. `sdfh_cli -img=my_docker_image -hap=my_heroku_app_name -r=flask_app_runner`

2. `sdfh_cli --image_name=my_docker_image --heroku_app_name=my_heroku_app_name --run=flask_app_runner`

Output 
```
./Dockerfile
./steps.txt
```
