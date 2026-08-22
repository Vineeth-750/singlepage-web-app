from django.test import TestCase
from django.urls import reverse

from .models import UserDetails


class UserDetailsModelTest(TestCase):

    def test_user_details_creation(self):
        user = UserDetails.objects.create(
            name="Vineeth",
            age=25,
            phone="9876543210",
            address="Kochi, Kerala"
        )

        self.assertEqual(user.name, "Vineeth")
        self.assertEqual(user.age, 25)
        self.assertEqual(user.phone, "9876543210")
        self.assertEqual(user.address, "Kochi, Kerala")


class UserDetailsViewTest(TestCase):

    def test_get_user_form(self):
        response = self.client.get(reverse("user_form"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_post_user_form(self):
        data = {
            "name": "Vineeth",
            "age": 25,
            "phone": "9876543210",
            "address": "Kochi, Kerala"
        }

        response = self.client.post(
            reverse("user_form"),
            data
        )

        self.assertEqual(response.status_code, 302)

        self.assertEqual(UserDetails.objects.count(), 1)

        user = UserDetails.objects.first()

        self.assertEqual(user.name, "Vineeth")
        self.assertEqual(user.age, 25)
        self.assertEqual(user.phone, "9876543210")
        self.assertEqual(user.address, "Kochi, Kerala")


class UserDetailsURLTest(TestCase):

    def test_user_form_url(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)