"""
PlanetTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .planet import Planet
from .planet_collection import PlanetCollection

class PlanetTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get_all(self, search: str) -> PlanetCollection:
        """
        Get all the planets
        """
        try:
            path_params = {}

            query_params = {}
            query_params['search'] = search

            query_struct_names = []

            url = self.parser.url('/planets', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = PlanetCollection.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get(self, id: str) -> Planet:
        """
        Get a specific planet
        """
        try:
            path_params = {}
            path_params['id'] = id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/planets/:id', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = Planet.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))



