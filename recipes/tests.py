import os
import json
from django.conf import settings
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile

# Mock json data
mock_data = [
    {"postcode": "10224", "recipe": "Creamy Dill Chicken", "delivery": "Wednesday 1AM - 7PM"},
    {"postcode": "10208", "recipe": "Speedy Steak Fajitas", "delivery": "Thursday 7AM - 5PM"},
]

class RecipesAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.json_file_path = os.path.join(settings.BASE_DIR, 'data.json')
        self.file_content = json.dumps(mock_data).encode('utf-8')
        self.uploaded_file = SimpleUploadedFile("data.json", self.file_content, content_type="application/json")

    def test_file_upload(self):
        response = self.client.post('/api/upload-recipes-file/', {'file': self.uploaded_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "File uploaded successfully."})

    def test_find_unique_recipes(self):

        # Ensure the file is uploaded and loaded
        self.client.post('/api/upload-recipes-file/', {'file': self.uploaded_file}, format='multipart')

        response = self.client.get('/api/find-unique-recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"unique_recipe_count": 2})

    def test_count_unique_recipe_occurrences(self):

        # Ensure the file is uploaded and loaded
        self.client.post('/api/upload-recipes-file/', {'file': self.uploaded_file}, format='multipart')

        response = self.client.get('/api/count-unique-recipes-occurrances/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "count_per_recipe": [
                {"recipe": "Creamy Dill Chicken", "count": 1},
                {"recipe": "Speedy Steak Fajitas", "count": 1}
            ]
        })

    def test_find_most_delivered_postcode(self):

        # Ensure the file is uploaded and loaded
        self.client.post('/api/upload-recipes-file/', {'file': self.uploaded_file}, format='multipart')

        response = self.client.get('/api/find-most-delivered-recipe/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "busiest_postcode": {
                "postcode": "10224",
                "delivery_count": 1
            }
        })

    def test_find_matching_recipes(self):

        # Ensure the file is uploaded and loaded
        self.client.post('/api/upload-recipes-file/', {'file': self.uploaded_file}, format='multipart')

        response = self.client.get('/api/find-matching-recipes/', {'keywords': 'Speedy'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"match_by_name": ["Speedy Steak Fajitas"]})

