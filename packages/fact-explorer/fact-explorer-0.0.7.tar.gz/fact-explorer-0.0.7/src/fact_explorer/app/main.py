from json import loads
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fact_explorer.app.business import search

from fact_explorer.app.db.db_session import db_instance as database_instance
from fact_explorer.app.entities.fact import FactOut
from fact_explorer.app.frontend.router import router as fe_router
from fact_explorer.config import get_configuration

from typing import Any, Dict, List
from cryptoshred.backends import DynamoDbSsmBackend
from pathlib import Path

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(
        directory=str(Path(__file__).resolve().parent.joinpath("frontend/static"))
    ),
    name="static",
)

app.include_router(fe_router)


@app.on_event("startup")
async def startup() -> None:
    await database_instance.connect()
    config = get_configuration()
    app.state.db = database_instance
    app.state.key_backend = DynamoDbSsmBackend(
        iv_param=config.cryptoshred_init_vector_path
    )


@app.get("/favicon.ico", include_in_schema=False)
async def favicon() -> FileResponse:
    return FileResponse(Path(__file__).parent.joinpath("frontend/static/favicon.png"))


@app.get("/", include_in_schema=False)
async def frontend_redirect() -> RedirectResponse:
    return RedirectResponse(url="/fe/")


@app.get("/health-check")
async def health_check() -> bool:
    return True


@app.get("/api/search", response_model=List[FactOut])
async def root(
    skip: int = 0,
    limit: int = 20,
    hq: str = "{}",
    pq: str = "{}",
    decrypt: bool = False,
) -> List[Dict[str, Any]]:
    """
    Query the Facts received. Results are ordered by when the where received.
    Newest first.

    - `skip`: skip the X newest entries
    - `limit`: display X facts
    - `hq`: the header query. Use query by example here
    Just send a dict of what you are looking for.
    - `pq`: the payload query. Use query by example here.
    Just send a dict of what you are looking for.
    - `decrypt`: whether or not to decrypt cryptoshred information
    (Caution might increase response time significantly)
    """
    result = await search.strict(
        db=app.state.db,
        key_backend=app.state.key_backend,
        skip=skip,
        limit=limit,
        hq=loads(hq),
        pq=loads(pq),
        decrypt=decrypt,
    )
    return result


@app.get("/api/last", response_model=List[FactOut])
async def last(minutes: int = 15, decrypt: bool = False) -> List[Dict[str, Any]]:
    """
    Displays the Facts received in the last X minutes. Results are ordered,
    newest first.

    Beware that this is a very expensive operations in terms of memory and time.
    Use with care, you will kill the application if you use to large values.

    - `minutes`: How many minutes from now backwards you want to get.
    - `decrypt`: whether or not to decrypt cryptoshred information
    (Caution might increase response time significantly)
    """
    result = await search.time_interval(
        db=app.state.db,
        key_backend=app.state.key_backend,
        minutes=minutes,
        decrypt=decrypt,
    )
    return result
