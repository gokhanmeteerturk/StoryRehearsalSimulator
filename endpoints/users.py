from fastapi import APIRouter, HTTPException, Query

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

import settings

router = APIRouter()

templates = Jinja2Templates(directory="templates")


# templates.env.globals['projectname'] = "Project Name"

@router.get("/", response_class=HTMLResponse)
async def giveaway(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request},
    )
