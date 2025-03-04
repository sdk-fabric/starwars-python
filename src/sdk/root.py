"""
root automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class Root(BaseModel):
    films: Optional[str] = Field(default=None, alias="films")
    people: Optional[str] = Field(default=None, alias="people")
    planets: Optional[str] = Field(default=None, alias="planets")
    species: Optional[str] = Field(default=None, alias="species")
    starships: Optional[str] = Field(default=None, alias="starships")
    vehicles: Optional[str] = Field(default=None, alias="vehicles")
    pass


