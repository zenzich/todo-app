from fastapi import FastAPI

from app.db.session import engine
from app.api.routes.tasks import router as tasks_router
from app.api.routes.categories import router as categories_router
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.db.base_class import Base
from app.core.config import settings

@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=[settings.ALLOWED_ORIGINS],
    allow_methods=["*"],
)
print(settings.ALLOWED_ORIGINS)
app.include_router(tasks_router)
app.include_router(categories_router)