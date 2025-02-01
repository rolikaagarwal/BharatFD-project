from django.test import TestCase
from .models import FAQ
from django.urls import reverse
from rest_framework.test import APITestCase


class FAQModelTests(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(
            question="What is Django?", answer="Django is a web framework."
        )

        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.answer, "Django is a web framework.")

    def test_faq_translation(self):
        faq = FAQ.objects.create(
            question="What is Django?", answer="Django is a web framework."
        )

        self.assertEqual(faq.get_translated_question("hi"), faq.question_hi)
        self.assertEqual(faq.get_translated_answer("hi"), faq.answer_hi)

        self.assertEqual(faq.get_translated_question("bn"), faq.question_bn)
        self.assertEqual(faq.get_translated_answer("bn"), faq.answer_bn)


class FAQAPITests(APITestCase):
    def setUp(self):
        # Create an FAQ for testing
        self.faq = FAQ.objects.create(
            question="What is Django?", answer="Django is a web framework."
        )

    def test_faq_list_view(self):
        # Get the API response
        url = reverse("faq-list")
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the FAQ is in the response
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["question"], "What is Django?")
        self.assertEqual(response.data[0]["answer"], "Django is a web framework.")

    def test_faq_list_view_with_language(self):
        # Get the API response with language parameter
        url = reverse("faq-list") + "?lang=hi"
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the translated FAQ is in the response
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["question"], self.faq.question_hi)
        self.assertEqual(response.data[0]["answer"], self.faq.answer_hi)
