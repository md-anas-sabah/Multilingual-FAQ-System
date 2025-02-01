# faqs/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import FAQ

class FAQModelTests(TestCase):
    def setUp(self):
        FAQ.objects.all().delete()
        self.faq = FAQ.objects.create(
            question="Test Question?",
            answer="Test Answer",
            question_hi="टेस्ट प्रश्न?",
            answer_hi="टेस्ट उत्तर"
        )

    def test_translation_fallback(self):
        self.assertEqual(self.faq.get_question('en'), "Test Question?")
        self.assertEqual(self.faq.get_question('hi'), "टेस्ट प्रश्न?")
        self.assertEqual(self.faq.get_question('bn'), "Test Question?")

class FAQAPITests(APITestCase):
    def setUp(self):
        FAQ.objects.all().delete()
        self.faq = FAQ.objects.create(
            question="API Test?",
            answer="API Answer"
        )
        self.url = reverse('faq-list')

    def test_get_faqs(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_language_parameter(self):
        response = self.client.get(f"{self.url}?lang=hi")
        self.assertEqual(response.status_code, status.HTTP_200_OK)