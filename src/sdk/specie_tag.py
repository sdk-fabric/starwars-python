"""
SpecieTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .specie import Specie
from .specie_collection import SpecieCollection

class SpecieTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get_all(self, search: str) -> SpecieCollection:
        """
        Get all the species
        """
        try:
            path_params = {}

            query_params = {}
            query_params["search"] = search

            query_struct_names = []

            url = self.parser.url("/species", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return SpecieCollection.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get(self, id: str) -> Specie:
        """
        Get a specific specie
        """
        try:
            path_params = {}
            path_params["id"] = id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/species/:id", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return Specie.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


