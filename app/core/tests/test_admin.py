"""
Test for the django admin modifications.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for Django Admin."""

    def setUp(self):
        """Create user and client."""
        self.Client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='user@example.com',
            password='testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )
