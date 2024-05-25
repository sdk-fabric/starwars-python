"""
vehicle automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
import datetime


# A Vehicle is a single transport craft that does not have hyperdrive capability
class Vehicle(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    model: Optional[str] = Field(default=None, alias="model")
    vehicle_class: Optional[str] = Field(default=None, alias="vehicle_class")
    manufacturer: Optional[str] = Field(default=None, alias="manufacturer")
    length: Optional[str] = Field(default=None, alias="length")
    cost_in_credits: Optional[str] = Field(default=None, alias="cost_in_credits")
    crew: Optional[str] = Field(default=None, alias="crew")
    passengers: Optional[str] = Field(default=None, alias="passengers")
    max_atmosphering_speed: Optional[str] = Field(default=None, alias="max_atmosphering_speed")
    cargo_capacity: Optional[str] = Field(default=None, alias="cargo_capacity")
    consumables: Optional[str] = Field(default=None, alias="consumables")
    films: Optional[List[str]] = Field(default=None, alias="films")
    pilots: Optional[List[str]] = Field(default=None, alias="pilots")
    url: Optional[str] = Field(default=None, alias="url")
    created: Optional[datetime.datetime] = Field(default=None, alias="created")
    edited: Optional[datetime.datetime] = Field(default=None, alias="edited")
    pass
