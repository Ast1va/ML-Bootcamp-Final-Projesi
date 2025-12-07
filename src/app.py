"""FastAPI entrypoint skeleton for serving predictions."""
from __future__ import annotations

from typing import Dict

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from src.config import AppConfig
from src.inference import predict_sample

app = FastAPI(title="Online Shoppers Intention Service")
config = AppConfig()
templates = Jinja2Templates(directory=str(config.template_dir))

EXPECTED_FIELDS = [
    "Administrative",
    "Administrative_Duration",
    "Informational",
    "Informational_Duration",
    "ProductRelated",
    "ProductRelated_Duration",
    "BounceRates",
    "ExitRates",
    "PageValues",
    "SpecialDay",
    "Month",
    "OperatingSystems",
    "Browser",
    "Region",
    "TrafficType",
    "VisitorType",
    "Weekend",
]
NUMERIC_FIELDS = {
    "Administrative",
    "Administrative_Duration",
    "Informational",
    "Informational_Duration",
    "ProductRelated",
    "ProductRelated_Duration",
    "BounceRates",
    "ExitRates",
    "PageValues",
    "SpecialDay",
    "OperatingSystems",
    "Browser",
    "Region",
    "TrafficType",
}


def _parse_form(form_data) -> Dict[str, object]:
    """Convert form data into a payload dict with basic casting."""
    payload: Dict[str, object] = {}
    for field in EXPECTED_FIELDS:
        raw_value = form_data.get(field)
        if raw_value is None:
            continue
        if field in NUMERIC_FIELDS:
            try:
                payload[field] = float(raw_value)
            except ValueError:
                payload[field] = 0.0
        elif field == "Weekend":
            payload[field] = raw_value.lower() in {"true", "1", "yes", "on"}
        else:
            payload[field] = str(raw_value)
    return payload


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": None,
            "values": {},
        },
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    form = await request.form()
    payload = _parse_form(form)
    try:
        result = predict_sample(payload)
    except FileNotFoundError as exc:
        message = "Model artifacts missing. Train a model before serving predictions."
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "result": {"error": message}, "values": payload},
            status_code=500,
        )
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result, "values": payload},
    )


@app.post("/predict.json")
async def predict_json(request: Request):
    body = await request.json()
    payload = {k: v for k, v in body.items() if k in EXPECTED_FIELDS}
    result = predict_sample(payload)
    return JSONResponse(result)
