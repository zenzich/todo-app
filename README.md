# todo-app
___
backend for todo app

# start
___

for start backend on windows use(you need docker desktop, python3.13)
```
docker run -e POSTGRES_PASSWORD=admin -p 15432:5432 -d postgres
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8080
```
backend url ```http://localhost:8080```