# Flask test server
Provide a basic flask api server for testing purposes

## Required Tech
* python 3.6+
* python venv

## How to run
* Navigate to the project root directory and create virtual environment using `python3 -m venv venv` and then activate it (optional)
* Execute `pip3 install -r requirements.txt` to install required modules
* Run `flask run` and enjoy :)

## How to use
Just open `app/__init__.py` file with your favourite text editor and modify content property in `/private` and `/public` routes to what ever you want

## Endpoints
### POST `/login`
* data: `{username: 'ahmedhrayyan', password: '123456'}`
* returns token to use in private endpoints
### GET `/private`
* private endpoint (requires Bearer token authorization)
* returns private data
### GET `/public`
* Public endpoint (doesn't require authorization)
* returns public data
