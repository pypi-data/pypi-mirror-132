# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.models.patchedansible_git_remote import PatchedansibleGitRemote  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException

class TestPatchedansibleGitRemote(unittest.TestCase):
    """PatchedansibleGitRemote unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchedansibleGitRemote
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_ansible.models.patchedansible_git_remote.PatchedansibleGitRemote()  # noqa: E501
        if include_optional :
            return PatchedansibleGitRemote(
                username = '0', 
                client_cert = '0', 
                tls_validation = True, 
                pulp_labels = None, 
                sock_connect_timeout = 0.0, 
                client_key = '0', 
                name = '0', 
                ca_cert = '0', 
                max_retries = 56, 
                rate_limit = 56, 
                connect_timeout = 0.0, 
                password = '0', 
                proxy_username = '0', 
                total_timeout = 0.0, 
                url = '0', 
                sock_read_timeout = 0.0, 
                proxy_password = '0', 
                download_concurrency = 1, 
                headers = [
                    None
                    ], 
                proxy_url = '0', 
                metadata_only = True, 
                git_ref = '0'
            )
        else :
            return PatchedansibleGitRemote(
        )

    def testPatchedansibleGitRemote(self):
        """Test PatchedansibleGitRemote"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
