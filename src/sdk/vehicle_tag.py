"""
VehicleTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .vehicle import Vehicle
from .vehicle_collection import VehicleCollection

class VehicleTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get_all(self, search: str) -> VehicleCollection:
        """
        Get all the vehicles
        """
        try:
            path_params = {}

            query_params = {}
            query_params["search"] = search

            query_struct_names = []

            url = self.parser.url("/vehicles", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return VehicleCollection.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get(self, id: str) -> Vehicle:
        """
        Get a specific vehicle
        """
        try:
            path_params = {}
            path_params["id"] = id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/vehicles/:id", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return Vehicle.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


