# Copyright 2022 Intel Corporation
# SPDX-License-Identifier: MIT
#
"""Test AutoSteer-G's TrinoDB connector"""
from connectors.trino_connector import TrinoConnector
from inference.preprocessing.preprocess_trino_plans import TrinoPlanPreprocessor
import unittest
import json

class TestTrinoConnector(unittest.TestCase):
    """TestCase for TrinoDB connector"""

    def setUp(self) -> None:
        self.connector = TrinoConnector()
        self.connector.connect()

    def tearDown(self) -> None:
        self.connector.close()

    def test_explain(self):
        with open('./test/data/expected_trino_plan.txt', 'r', encoding='utf-8') as f:
            expected_plan = ''.join(f.readlines())
        actual_plan = self.connector.explain('SELECT 42')
        self.assertEqual(actual_plan, json.loads(expected_plan))

    def test_execution(self):
        result = self.connector.execute('SELECT 42')
        self.assertEqual(result.result[0][0], 42)
        self.assertGreater(result.time_usecs, 0)

    def test_disable_knobs(self):
        knobs = TrinoConnector.get_knobs()
        self.connector.set_disabled_knobs([])
        # test that all knobs are turned on
        self.assertTrue(all(self.connector.get_knob(knob) for knob in knobs))
        self.connector.set_disabled_knobs(knobs)
        # test that all knobs are turned off
        self.assertTrue(not any(self.connector.get_knob(knob) for knob in knobs))
        # turn on all knobs
        self.connector.set_disabled_knobs([])
        self.assertTrue(all(self.connector.get_knob(knob) for knob in knobs))

    def test_num_knobs(self):
        self.assertEqual(len(TrinoConnector.get_knobs()), 7)

    def test_preprocessor(self):
        preprocessor = TrinoConnector.get_plan_preprocessor()
        self.assertEqual(preprocessor, TrinoPlanPreprocessor)


if __name__ == '__main__':
    unittest.main()
