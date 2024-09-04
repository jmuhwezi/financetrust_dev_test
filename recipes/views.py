import json
import os
from django.conf import settings
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import Counter

# Global variable to hold JSON file data
global_json_data = [] 

def load_json_data():
    # Load the file data into the global variable
    file_path = os.path.join(settings.BASE_DIR, 'data.json')
    with open(file_path, 'r') as json_file:
        global global_json_data
        global_json_data = json.load(json_file)


class RecipesFileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']

        # Save the uploaded file
        try:
            file_path = os.path.join(settings.BASE_DIR, 'data.json')
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            # load new uploaded file data into global variable
            load_json_data()

            return Response({"message": "File uploaded successfully."}, status=status.HTTP_200_OK)

        except KeyError:
            # Handle missing 'file' in request.FILES
            return Response({"error": "No file provided in the request."}, status=status.HTTP_400_BAD_REQUEST)

        except PermissionError:
            # Handle permission errors when writing to the file
            return Response({"error": "Permission denied. Unable to write file."}, status=status.HTTP_403_FORBIDDEN)

        except Exception as e:
            # Handle other exceptions
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FindUniqueRecipesView(APIView):
    def get(self, request, *args, **kwargs):

        # Load data from json file if global variable is not set
        if not global_json_data or len(global_json_data) == 0:
            load_json_data()

        # Count unique recipes
        unique_recipes = set([item['recipe'] for item in global_json_data])
        unique_recipe_count = len(unique_recipes)

        return Response({"unique_recipe_count": unique_recipe_count}, status=status.HTTP_200_OK)


class CountUniqueRecipeOccurencesView(APIView):
    def get(self, request, *args, **kwargs):

        # Load data from json file if global variable is not set
        if not global_json_data or len(global_json_data) == 0:
            load_json_data()

        recipe_count = Counter(item['recipe'] for item in global_json_data)

        # Format the results
        count_per_recipe = [
            {"recipe": recipe, "count": count}
            for recipe, count in sorted(recipe_count.items())
        ]

        return Response({"count_per_recipe": count_per_recipe}, status=status.HTTP_200_OK)


class FindMostDeliveredRecipeByPostCodeView(APIView):
    def get(self, request, *args, **kwargs):
        result = {
                "busiest_postcode": {
                    "postcode": None,
                    "delivery_count": 0
                }
            }

        # Load data from json file if global variable is not set
        if not global_json_data or len(global_json_data) == 0:
            load_json_data()

        postcode_count = Counter(item['postcode'] for item in global_json_data)

        # Get the most common postcode and its count
        if postcode_count:
            most_delivered_postcode, delivery_count = postcode_count.most_common(1)[0]

            # Format the result
            result = {
                "busiest_postcode": {
                    "postcode": most_delivered_postcode,
                    "delivery_count": delivery_count
                }
            }

        return Response(result, status=status.HTTP_200_OK)


class FindMatchingRecipesView(APIView):
    def get(self, request, *args, **kwargs):

        # Load data from json file if global variable is not set
        if not global_json_data or len(global_json_data) == 0:
            load_json_data()

        # by default find match recipes of ['Potato', 'Veggie', 'Mushroom'] if no params sent over api
        keywords = request.query_params.getlist('keywords', ['Potato', 'Veggie', 'Mushroom'])
        matching_recipes = sorted(set( item['recipe'] for item in global_json_data if any(keyword in item['recipe'] for keyword in keywords)))

        return Response({"match_by_name": matching_recipes})

