from django.contrib.auth import get_user_model
from django.test import TestCase


class TestAdminPanel(TestCase):
    def test_list_display(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            password='<PASSWORD>',
        )
        self.client.force_login(self.admin_user)
        url = "/admin/taxi/driver/"
        res = self.client.get(url)
        self.assertContains(res, "License number")

