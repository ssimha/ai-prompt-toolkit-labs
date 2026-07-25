"""
The Pydantic contract from section 4.3 — reviewed and approved in
isolation before any endpoint logic was written against it. If you
change these fields, remember the chapter's point: a partner system
may already be coded against the current shape.
"""

from datetime import date, datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class ShipmentStatus(str, Enum):
    pending = "pending"
    in_transit = "in_transit"
    delivered = "delivered"
    exception = "exception"


class ShipmentResponse(BaseModel):
    shipment_id: str
    status: ShipmentStatus
    estimated_delivery: Optional[date] = None
    last_updated: datetime
    carrier: str
