"""
The shipment status endpoint — this is Fenwick's "existing endpoint"
that section 4.4's few-shot prompt pulls its error-handling example
from. It intentionally uses estimate_delivery_buggy so the section 4.5
bug is live and reproducible; Exercise 1 has you find and fix it.
"""

from fastapi import APIRouter
from app.errors import APIError
from app.models import ShipmentResponse, ShipmentStatus
from app.db import get_shipment
from app.delivery import estimate_delivery_buggy, CARRIER_TIMEZONES

router = APIRouter()


@router.get("/shipments/{shipment_id}", response_model=ShipmentResponse)
def get_shipment_status(shipment_id: str) -> ShipmentResponse:
    shipment = get_shipment(shipment_id)

    if shipment is None:
        raise APIError(
            code="SHIPMENT_NOT_FOUND",
            status_code=404,
            detail=f"No shipment with id {shipment_id}",
        )

    if shipment["carrier"] not in CARRIER_TIMEZONES:
        raise APIError(
            code="INVALID_CARRIER",
            status_code=422,
            detail=f"Unknown carrier: {shipment['carrier']}",
        )

    status = ShipmentStatus(shipment["status"])

    estimated_delivery = None
    if status in (ShipmentStatus.pending, ShipmentStatus.in_transit):
        # NOTE: uses the buggy calculation on purpose — see app/delivery.py
        # and Chapter 4, section 4.5 / exercises/01_fix_timezone_bug.md
        estimated_delivery = estimate_delivery_buggy(
            shipment["pickup_utc"], shipment["transit_days"], shipment["carrier"]
        )

    return ShipmentResponse(
        shipment_id=shipment["shipment_id"],
        status=status,
        estimated_delivery=estimated_delivery,
        last_updated=shipment["last_updated"],
        carrier=shipment["carrier"],
    )
