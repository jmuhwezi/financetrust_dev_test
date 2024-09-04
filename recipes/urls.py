from django.urls import path
from recipes.views import RecipesFileUploadView, FindUniqueRecipesView, CountUniqueRecipeOccurencesView, \
FindMostDeliveredRecipeByPostCodeView, FindMatchingRecipesView

# app end-points
urlpatterns =[
    path('upload-recipes-file/', RecipesFileUploadView.as_view(), name='upload-recipes-file'),
    path('find-unique-recipes/', FindUniqueRecipesView.as_view(), name='find-unique-recipes'),
    path('count-unique-recipes-occurrances/', CountUniqueRecipeOccurencesView.as_view(), name='count-unique-recipes-occurrances'),
    path('find-most-delivered-recipe/', FindMostDeliveredRecipeByPostCodeView.as_view(), name='find-most-delivered-recipe'),
    path('find-matching-recipes/', FindMatchingRecipesView.as_view(), name='find-matching-recipes')
]