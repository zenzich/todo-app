from fastapi import FastAPI

from app.db.session import engine
from app.routes.tasks import router as tasks_router
from app.routes.categories import router as categories_router
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.db.base_class import Base

@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
)

app.include_router(tasks_router)
app.include_router(categories_router)