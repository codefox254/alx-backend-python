#!/usr/bin/env python3
"""Unit tests for GithubOrgClient.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos, apache2_repos_filtered
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", org_payload),
        ("abc", org_payload),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_response, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value.
        """
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_response)

    def test_public_repos_url(self):
        """Test the _public_repos_url property.
        """
        with patch("client.GithubOrgClient.org", return_value=org_payload):
            client = GithubOrgClient("example_org")
            self.assertEqual(client._public_repos_url, org_payload["repos_url"])

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", return_value="https://api.github.com/orgs/example_org/repos")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test the public_repos method.
        """
        mock_get_json.return_value = repos_payload
        client = GithubOrgClient("example_org")
        self.assertEqual(client.public_repos(), expected_repos)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method.
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)

class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the class for integration tests.
        """
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: org_payload),
            unittest.mock.Mock(json=lambda: repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down the class after integration tests.
        """
        cls.get_patcher.stop()

    @parameterized_class([
        {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos, "apache2_repos": apache2_repos},
    ])
    def test_public_repos(self, fixtures):
        """Test the public_repos method with integration tests.
        """
        client = GithubOrgClient("example_org")
        self.assertEqual(client.public_repos(), fixtures["expected_repos"])

    @parameterized_class([
        {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": apache2_repos, "apache2_repos": apache2_repos_filtered},
    ])
    def test_public_repos_with_license(self, fixtures):
        """Test the public_repos method with a license filter.
        """
        client = GithubOrgClient("example_org")
        self.assertEqual(client.public_repos(license="apache-2.0"), fixtures["apache2_repos"])

if __name__ == "__main__":
    unittest.main()
