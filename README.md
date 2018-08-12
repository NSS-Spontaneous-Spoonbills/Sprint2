# Spontaneous Spoonbills: Sprint 2

## To Run

1. Clone the repo.
1. Start your virtual environment
1. From the command line, cd into the root directory (wherever the manage.py file is located).
1. Type ```python manage.py runserver``` into the command line.
1. Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Naming Conventions

1. All branches to have lowercase initials 
1. File name to match class name and describe use 
1. Every function and class needs a docstring
1. Every model class needs a dunderscore string (__str__)
1. All model names and field names should match the ERD exactly

```
Ex. js_(branch_feature)
Employee_Model.py -> class Employee_Model
Employee_View.py -> class Employee_View
```

## Pull Request Conventions

1. Pull requests should include a list of which files were added, modified, or deleted in this PR so we can check for conflicts and scope of change.

## ERD Changes

* Computer ticket requires adding two new fields to computer model:
  * manufacturer
  * make
  * has_been_assigned

## Site URLs

* **Base URL**: http://127.0.0.1:8000/WorkforceManagement
* **Computer List**: http://127.0.0.1:8000/WorkforceManagement/computers/
* **Computer Detail**: http://127.0.0.1:8000/WorkforceManagement/computers/1 (or 2, 3, etc.)
* **New Computer Form**: http://127.0.0.1:8000/WorkforceManagement/computers/new
* **Update Computer Form**: http://127.0.0.1:8000/WorkforceManagement/computers/1/update/
* **Employee List**: http://127.0.0.1:8000/WorkforceManagement/employees/
* **Employee Detail**: http://127.0.0.1:8000/WorkforceManagement/employees/1/ (or 2, 3, etc.)
* **Department List**: http://127.0.0.1:8000/WorkforceManagement/departments/
* **Training Program List**: http://127.0.0.1:8000/WorkforceManagement/training_programs/

## Run Testing

1. To run tests on the current code
```
python manage.py test
```

## Currently Tests:

* **Employee Detail**
* **Employee List**