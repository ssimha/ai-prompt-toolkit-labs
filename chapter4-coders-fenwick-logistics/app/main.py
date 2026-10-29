from fastapi import FastAPI
from app.errors import register_exception_handlers
from app.routes.shipments import router as shipments_router

app = FastAPI(title="Fenwick Logistics — Shipment Tracking API")

register_exception_handlers(app)
app.include_router(shipments_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
