#!/usr/bin/env python3
"""A module for testing GithubOrgClient module"""
import requests
import unittest
from typing import Dict
from unittest.mock import (
        MagicMock,
        Mock,
        PropertyMock,
        patch,
        )
from client import (
        GithubOrgClient
        )
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """function for testing the GithubOrgClient class"""
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
        ])
    @patch(
            "client.get_json",
            )
    def test_org(self, org: str, resp: Dict, mocked_func: MagicMock) -> None:
        """Test the org method

        Args:
            org (str): _description_
            expected_response (Dictionary): _description_
            mocked_function (MagicMock): _description_
        """
        mocked_func.return_value = MagicMock(return_value=cor_resp)
        goc = GithubOrgClient(org)
        self.assertEqual(goc.org(), cor_resp)
        mocked_func.assert_called_once_with(
                f"https://api.github.com/orgs/{org}"
                )

        def test_public_repos_url(self) -> None:
            """A public repository url test function"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                    "repos_url": "https://api.github.com/users/google/repos",
                    }
            self.assertEqual(
                    GithubOrgClient("google")._public_repos_url,
                    "https://api.github.com/users/google/repos",
                    )

            @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Function that test the public repos

        Args:
             mock_get_json(MagicMock): _description_
        """
        test_payload = {
            "repos_url": "https://api.github.com/users/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-05T05:10:38Z",
                    "updated_at": "2024-11-05T05:11:45Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2024-11-05T05:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                    },
                ]
            }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                    GithubOrgClient("google").public_repos(),
                    [
                        "episodes.dart",
                        "kratu",
                        ],
                    )
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, resp: bool) -> None:
        """A function that test the has license method."""
        goc = GothubOrgClient("google")
        client_has_license = goc.has_license(repo, key)
        self.assertEqual(client_has_license, resp)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
        },
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """class that performs integration tests for GithubOrgClient"""
    @classmethod
    def setUpClass(cls) -> None:
        """Set up class fixtures for running"""
        route_payload = {
                "https://api.github.com/orgs/google": cls.org_payload,
                "https://api.github.com/orgs/google/repos": cls.repos_payload,
                }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{"json.return_value": route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Test public repos method."""
        self.assertEqual(
                GithubOrgClient("google").public_repos(),
                self.expected_repos,
                )

        def test_public_repos_with_license(self) -> None:
            """Test public repository with a license."""
        self.assertEqual(
                GithubOrgClient("google").public_repos(license="apache-2.0"),
                self.apache2_repos,
                )

        @classmethod
    def tearDownClass(cls) -> None:
        """A function that removes the class fixtures
        after running all tests
        """
        cls.get_patcher.stop()
