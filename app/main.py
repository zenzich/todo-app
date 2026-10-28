from fastapi import FastAPI
from app.routes.tasks import router as tasks_router
from app.routes.categories import router as categories_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
)

app.include_router(tasks_router)
app.include_router(categories_router)