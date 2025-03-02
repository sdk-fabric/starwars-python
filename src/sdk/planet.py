"""
planet automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
import datetime


# A Planet is a large mass, planet or planetoid in the Star Wars Universe, at the time of 0 ABY
class Planet(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    diameter: Optional[str] = Field(default=None, alias="diameter")
    rotation_period: Optional[str] = Field(default=None, alias="rotation_period")
    orbital_period: Optional[str] = Field(default=None, alias="orbital_period")
    gravity: Optional[str] = Field(default=None, alias="gravity")
    population: Optional[str] = Field(default=None, alias="population")
    climate: Optional[str] = Field(default=None, alias="climate")
    terrain: Optional[str] = Field(default=None, alias="terrain")
    surface_water: Optional[str] = Field(default=None, alias="surface_water")
    residents: Optional[List[str]] = Field(default=None, alias="residents")
    films: Optional[List[str]] = Field(default=None, alias="films")
    url: Optional[str] = Field(default=None, alias="url")
    created: Optional[datetime.datetime] = Field(default=None, alias="created")
    edited: Optional[datetime.datetime] = Field(default=None, alias="edited")
    pass


