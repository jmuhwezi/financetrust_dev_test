# Recipe Statistics API 

This project provides a set of API endpoints to process automatically generate a JSON file with data and calculate statistics.

## Project Tasks
1. Count the number of unique recipe names.
2. Count the number of occurences for each unique recipe name (alphabetically ordered by recipe name).
3. Find the postcode with most delivered recipes.
4. List the recipe names (alphabetically ordered) that contain in their name one of the following words:
   - Potato
   - Veggie
   - Mushroom
## Stacks

- Python 3.7 and above
- Django 3.2.15
- Django rest framework 3.14.0

## Prerequisites
- Virtual env't.
- Docker
- Docker Compose

## Setup Steps

1. **Clone the repository**:
    ```sh
    git clone git@github.com:jmuhwezi/financetrust_dev_test.git
    cd financetrust_dev_test/
    git fetch origin Muhwezi_Jerald_ftb_dev
    git checkout Muhwezi_Jerald_ftb_dev
    ```

2. **Ensure Docker is up and running**:
    ```sh
    docker-compose build
    docker-compose up
    ```

2. **Accessing the application**:

    - **Base Url:**: [http://localhost:8000/](http://localhost:8000/)
    - **Custom Json File Upload**: [http://localhost:8000/api/upload-recipes-file/](http://localhost:8000/api/upload-recipes-file/). This is for updating/uploading new json file.
    - **Unique Recipe Count**: [http://localhost:8000/api/find-unique-recipes/](http://localhost:8000/api/find-unique-recipes/).
    - **Count Per Recipe**: [http://localhost:8000/api/count-unique-recipes-occurrances/](http://localhost:8000/api/count-unique-recipes-occurrances/).
    - **Busiest Postcode**: [http://localhost:8000/api/find-most-delivered-recipe/](http://localhost:8000/api/find-most-delivered-recipe/). 
    - **Matched Recipe Names**: [http://localhost:8000/api/find-matching-recipes/?keywords=Potato&keywords=Veggie](http://localhost:8000/api/find-matching-recipes/?keywords=Potato&keywords=Veggie).
