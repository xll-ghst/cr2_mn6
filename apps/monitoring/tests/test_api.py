from unittest.mock import patch

from django.core.cache import cache
from rest_framework.test import APITestCase


class MonitoringApiTests(APITestCase):
    def setUp(self):
        cache.clear()

    def test_stats_endpoint_returns_statistics(self):
        response = self.client.get("/api/v1/stats/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"users_count": 1000, "active_orders": 42})

    @patch("apps.monitoring.services.send_welcome_email_task.delay")
    def test_register_queues_email_and_returns_201(self, mocked_delay):
        response = self.client.post(
            "/api/v1/register/", {"email": "test@example.com"}, format="json"
        )
        self.assertEqual(response.status_code, 201)
        mocked_delay.assert_called_once_with("test@example.com")

    def test_register_rejects_invalid_email(self):
        response = self.client.post(
            "/api/v1/register/", {"email": "not-an-email"}, format="json"
        )
        self.assertEqual(response.status_code, 400)
