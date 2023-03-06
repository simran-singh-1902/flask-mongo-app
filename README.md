## Backend python assessment

***Code Navigation***

This project consists of a main folder `src` which contains all the project files. The files outside the source folder consists of `docker-compose.yml`, `Dockerfile` and a `local.env` file which are used for running the docker containers. The `src` folder contains the entrypoint of the Flask project `app.py`, `settings` folder which contains your application settings and an `apis` folder that stores all your urls and views.

Specify the urls in `urls.py` file in the api folder as list of tuples with following format:

    (endpoint, view_func, methods, description)
example:

    ("/", views.index, ["GET"], "index page")

***Installation***

Running the scaffolding app is very easy. First [install](https://docs.docker.com/install/) docker for your operating system from the docs provided in the docker website. Also [install](https://docs.docker.com/compose/install/) docker-compose

For mac m1 chip export these variables:

    export DOCKER_BUILDKIT=0   
    export COMPOSE_DOCKER_CLI_BUILD=0      
    
Then run

    sudo docker-compose build
and then

    sudo docker-compose up
This will run the server at port http://localhost:8400/

The index view will be displayed in your browser.

***Logs***

A `logs` folder is created in the root of the project i.e outside the `src` folder, which is mounted using the docker-compose volume mount. It will contain a file `flask-scaffolding.log` and will contain the project logs.

***APIS***

Start by adding dummy users for now - 

    http://localhost:8400/add-users
    method = GET

the above url will add dummy users for now to your mongodb collection

For logging in -

    http://localhost:8400/login
    method = POST
    Payload = {
    "username": "Simran",
    "password": "123"
    }

For creating user -

    http://localhost:8400/create-user
    method = POST
    Payload = {
        "first_name":"Simran",
        "last_name":"Singh",
        "email":"Simran@gmail.com",
        "username":"Simran",
        "password": 123
        }

List all users - 
    
    http://localhost:8400/get-users
    method = GET