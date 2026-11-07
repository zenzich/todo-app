<div align="center">

# todo-app


![python version](https://img.shields.io/badge/python-3.13-green)
![fastapi](https://img.shields.io/badge/FastAPI-blue)
![postgreSQL](https://img.shields.io/badge/PostgreSQL-blue)
![redis](https://img.shields.io/badge/Redis-blue)
![architecture](https://img.shields.io/badge/architecture-layered-purple)
![async](https://img.shields.io/badge/async-yes-purple)
</div>

**todo-app** &mdash; a simple to-do list application built as a pet project.

## Architecture

```text
/app/
  api/
      routes/
  cashe/
  core/
  db/
      models/
  repos/
  schemas/
  services/
```


## Start

* You need installed [*docker*](https://docs.docker.com/desktop/) on your PC
* Open docker desktop
* For start backend use: (use it only in **\todo-app** directory)
```bash
docker-compose up --build
```
After start you can check backend [*here*](http://localhost:8080) (```http://localhost:8080```)