"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import qaseio
from qaseio.api.cases_api import CasesApi  # noqa: E501


class TestCasesApi(unittest.TestCase):
    """CasesApi unit test stubs"""

    def setUp(self):
        self.api = CasesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bulk(self):
        """Test case for bulk

        Create test cases in bulk.  # noqa: E501
        """
        pass

    def test_create_case(self):
        """Test case for create_case

        Create a new test case.  # noqa: E501
        """
        pass

    def test_delete_case(self):
        """Test case for delete_case

        Delete test case.  # noqa: E501
        """
        pass

    def test_get_case(self):
        """Test case for get_case

        Get a specific test case.  # noqa: E501
        """
        pass

    def test_get_cases(self):
        """Test case for get_cases

        Get all test cases.  # noqa: E501
        """
        pass

    def test_update_case(self):
        """Test case for update_case

        Update test case.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
