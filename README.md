# Spontaneous Spoonbills: Sprint 2

## To Run

1. Clone the repo.
1. Start your virtual environment
1. From the command line, cd into the root directory (wherever the manage.py file is located).
1. Type ```python manage.py runserver``` into the command line.
1. Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Conventions

1. All branches to have lowercase initials 
1. File name to match class name and describe use 
1. Every function and class needs a docstring
1. Every function needs a dunderscore string (__str__)
1. All model names and field names should match the ERD exactly

```
Ex. js_(branch_feature)
Employee_Model.py -> class Employee_Model.py
Employee_View.py -> class Employee_View.py
```

## ERD Changes

* Computer ticket requires adding two new fields to computer model:
  * manufacturer
  * make