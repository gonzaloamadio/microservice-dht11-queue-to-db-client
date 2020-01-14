# First steps with microservices

Follow this tutorial : [Tutorial](https://www.cloudamqp.com/blog/2019-09-11-a-developers-guide-through-the-microservice-jungle.html)

But I replaced the raspberry pi script, with a python script, as I do not have a raspberry.

For this, I followed: [Doc](https://www.cloudamqp.com/docs/python.html)

# Technologies used

- Microservices (ok, this is not a tech, but it is worth mentioning because it is the objective of this project)
- Python
- Heroku
- RabbitQM
- ElephantSQL (PostgreSQL)

# Heroku

## Add env variables

[Doc of how to add an ENV variable](https://devcenter.heroku.com/articles/config-vars)

```
heroku config:set GITHUB_USERNAME=joesmith
heroku config
```

# Usage

To use it locally, you can run in different terminals the python microservices.

```
$ python microservice01-raspberry.py
sending data
sending data
```

```
python microservice02-store-data-in-db.py  

[*] Waiting for messages:

[X] Received time:1579041490.4134362 and temperature: 0.49375389629322086
1 Record inserted successfully into weather table
PostgreSQL connection is closed
[X] Received time:1579041490.4134362 and temperature: 0.49375389629322086
1 Record inserted successfully into weather table
PostgreSQL connection is closed
```
