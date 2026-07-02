import os
from unittest import TestCase
from unittest.mock import patch

from fastapi.testclient import TestClient

from api.app import app


class ApiAuthTests(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_request_passes_when_api_key_is_not_configured(self):
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("COMPASS_API_KEY", None)

            response = self.client.get("/api/v1/companies")

        self.assertEqual(response.status_code, 200)

    def test_request_is_rejected_when_api_key_is_missing(self):
        with patch.dict(os.environ, {"COMPASS_API_KEY": "test-secret"}, clear=False):
            response = self.client.get("/api/v1/companies")

        self.assertEqual(response.status_code, 401)

    def test_request_passes_when_api_key_matches(self):
        with patch.dict(os.environ, {"COMPASS_API_KEY": "test-secret"}, clear=False):
            response = self.client.get("/api/v1/companies", headers={"X-API-Key": "test-secret"})

        self.assertEqual(response.status_code, 200)

    def test_health_is_not_api_key_protected(self):
        with patch.dict(os.environ, {"COMPASS_API_KEY": "test-secret"}, clear=False):
            response = self.client.get("/api/v1/health")

        self.assertEqual(response.status_code, 200)
