import time
from typing import Callable, Awaitable
from fastapi import Request
from server import LOGGER
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class LoggerMiddleWare(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        LOGGER.info(f"[{request.method}]-> {request.url.path} Called")
        start_time = time.time()
        response = await call_next(request)
        end_time = time.time() - start_time
        LOGGER.info(
            f"[{request.method}]-> {request.url.path} Finished. Status Code : {response.status_code} | Total Time : {end_time}"
        )
        return response
