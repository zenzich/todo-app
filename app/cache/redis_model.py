import json

import redis.asyncio as redis

class RedisCache:
    def __init__(self, redis_url: str, ttl_seconds: int | None = None):
        self.redis = redis.from_url(redis_url, decode_responses=True)
        self.ttl_seconds = ttl_seconds

    async def set(self, key: str, value: dict) -> None:
        await self.redis.set(key, json.dumps(value), ex=self.ttl_seconds)

    async def get(self, key: str) -> dict:
        return json.loads(await self.redis.get(key))

    async def delete(self, key: str) -> None:
        await self.redis.delete(key)