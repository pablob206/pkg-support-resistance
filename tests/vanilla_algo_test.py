"""ML Models Exploration Test"""

from typing import Dict, Any
import json
from src.pkg_support_resistance import VanillaSupportResistance
from .expected_output_test import vanilla_sr_exec_pipeline_expected_output_test


def open_json_file(input_file_path: str, mode: str = "r") -> Dict[str, Any]:
    """Open json file"""

    with open(file=input_file_path, mode=mode) as file:
        data = json.load(file)
    return data


def test_vanilla_support_resistance_exec_pipeline():
    """
    Test the calculation of support/resistance process.
    This test verifies that the function exec_pipeline,
    returns the expected output given a specific input file path and cluster threshold.
    """

    input_file_path = "../src/pkg_support_resistance/data_set/example.json"
    input_data: dict = open_json_file(input_file_path=input_file_path)

    result: list[dict] = VanillaSupportResistance.exec_pipeline(
        input_data=input_data, cluster_threshold=1
    )
    assert result == vanilla_sr_exec_pipeline_expected_output_test
