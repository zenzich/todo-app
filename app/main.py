from fastapi import FastAPI
from routes.tasks import router as tasks_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
)

app.include_router(tasks_router)