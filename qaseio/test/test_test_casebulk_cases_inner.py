# coding: utf-8

"""
    Qase.io TestOps API

    Qase TestOps API Specification.

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from qaseio.models.test_casebulk_cases_inner import TestCasebulkCasesInner

class TestTestCasebulkCasesInner(unittest.TestCase):
    """TestCasebulkCasesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestCasebulkCasesInner:
        """Test TestCasebulkCasesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestCasebulkCasesInner`
        """
        model = TestCasebulkCasesInner()
        if include_optional:
            return TestCasebulkCasesInner(
                description = '',
                preconditions = '',
                postconditions = '',
                title = '',
                severity = 56,
                priority = 56,
                behavior = 56,
                type = 56,
                layer = 56,
                is_flaky = 56,
                author_id = 56,
                suite_id = 56,
                milestone_id = 56,
                automation = 56,
                status = 56,
                attachments = [
                    ''
                    ],
                steps = [
                    qaseio.models.test_step_create.TestStepCreate(
                        action = '', 
                        expected_result = '', 
                        data = '', 
                        position = 56, 
                        attachments = [
                            ''
                            ], )
                    ],
                tags = [
                    ''
                    ],
                params = {
                    'key' : [
                        ''
                        ]
                    },
                custom_field = {
                    'key' : ''
                    },
                created_at = '',
                updated_at = '',
                id = 56
            )
        else:
            return TestCasebulkCasesInner(
                title = '',
        )
        """

    def testTestCasebulkCasesInner(self):
        """Test TestCasebulkCasesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
