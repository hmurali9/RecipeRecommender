# RecipeRecommender

## Setup Instructions
1. From base directory of repo create conda environment with 'conda env create -f environment.yml'
2. Activate conda environment with 'conda activate reciperecommender'
3. Update existing environment with 'conda env update --prune -f environment.yml' as needed

## Usage Instructions
1. Run using 'python app.py'
2. Open url http://127.0.0.1:5000 to view output

## Overview

1. app.py contains code to launch a flask based web application
2. Necessary HTML templates are stored within *templates* folder
3. All function referenced in it are stored under *allFunctions* folder
4. All classes referenced in it are stored under *allClasses* folder
5. Datasets for recipes, ingredients and recipe to ingredient link are stored as csv files under *data* folder
