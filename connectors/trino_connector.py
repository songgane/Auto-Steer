# Copyright 2022 Intel Corporation
# SPDX-License-Identifier: MIT
#
"""This module provides several helper functions to connect to trino server"""
from typing import Type
import trino as trinodb
import connectors.connector
from connectors.connector import DBConnector
import configparser
import os
from inference.preprocessing.preprocess_trino_plans import TrinoPlanPreprocessor
from inference.preprocessing.preprocessor import QueryPlanPreprocessor
import json

class TrinoConnector(DBConnector):
    """This class wraps a Trino session"""

    def __init__(self, knobs: list = None):
        super().__init__()
        self.config = configparser.ConfigParser()
        self.config.read(os.path.dirname(__file__) + '/../configs/trino.cfg')
        self.session_properties = {}

        if knobs:
            self.set_disabled_knobs(knobs)
            
        self.connect()

    def connect(self) -> None:
        defaults = self.config['DEFAULT']
        self.session_properties['query_max_execution_time'] = defaults['execution_timeout']
        self.connection: trinodb.dbapi.Connection = trinodb.dbapi.connect(
            host=defaults['host'],
            port=defaults['port'],
            user=defaults['user'],
            catalog=defaults['catalog'],
            schema=defaults['schema'],
            request_timeout=trinodb.constants.DEFAULT_REQUEST_TIMEOUT,
            session_properties=self.session_properties,
        )

    def close(self) -> None:
        self.connection.close()

    def execute(self, query) -> connectors.connector.DBConnector.TimedResult:
        cur = self.connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return connectors.connector.DBConnector.TimedResult(result, cur.stats['elapsedTimeMillis'] * 1_000, cur.stats['physicalInputBytes'], cur.stats['nodes'])

    def set_disabled_knobs(self, knobs: list) -> None:
        all_knobs = TrinoConnector.get_knobs()
        for knob in all_knobs:
            self.session_properties[knob] = True
        for knob in knobs:
            self.session_properties[knob] = False

    def merge_to_parent(self, childrens, root):
        for child in childrens:
            if child.get('descriptor') and child.get('descriptor').get('sourceFragmentIds'):
                l = list()
                ids = json.loads(child.get('descriptor').get('sourceFragmentIds'))
                for id in ids:
                    l.append(root.get(str(id)))
                child['children'] = list(filter(None, l))
            else:
                self.merge_to_parent(child['children'], root)

    def convert_to_nested_childrens(self, root:dict) -> dict:
        trees = []

        for k, v in root.items():
            self.merge_to_parent(v.get('children'), root)  
        
        trees = list(root.values())

        if len(trees) > 0:
            return trees[0]
        else:
            return None

    #FIXME: trino explain json을 presto explain json의 형태로 변경한다.
    def explain(self, query) -> str:
        timed_result = self.execute('EXPLAIN (FORMAT JSON) ' + query)
        netsted_timed_result = self.convert_to_nested_childrens(json.loads(timed_result.result[0][0]))
        return json.dumps(netsted_timed_result)
        # The query plan is already properly formatted as Json string
        # return timed_result.result[0][0]

    def _get_connection(self) -> trinodb.dbapi.Connection:
        return self.connection

    def set_catalog(self, catalog):
        self.connection.catalog = catalog

    def set_schema(self, schema):
        self.connection.schema = schema

    def get_knob(self, knob: str) -> bool:
        return self.session_properties[knob]

    @staticmethod
    def get_plan_preprocessor() -> Type[QueryPlanPreprocessor]:
        """Return the type of the query plan preprocessor"""
        return TrinoPlanPreprocessor

    @staticmethod
    def get_name() -> str:
        return 'trino'

    @staticmethod
    def get_knobs() -> list:
        """Static method returning all knobs defined for this connector"""
        with open(os.path.dirname(__file__) + '/../knobs/trino_top_7.txt', 'r', encoding='utf-8') as f:
            return [line.replace('\n', '') for line in f.readlines()]
