# Med Lexicon

Med Lexicon is a Django-based web application designed for managing medical vocabulary. Users can add, edit, delete, and view medical terms across different categories and formats. The application also supports employee (worker) management, allowing for the assignment of staff to tasks like word management.

## Check it out!
https://medical-e-dictionary.onrender.com

- Login information:
  - Username: `test_user`
  - Password: `zaqwsx5432`

## Installing / Getting started

Python3 must be already installed

```shell
git clone https://github.com/yaroslavsysoiev/med_lexicon
cd med_lexicon
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Features

- **Word Management**: Add, edit, delete, and view words in multiple languages (e.g., English, Ukrainian, Polish).
- **Category and Format Organization**: Group words by categories and formats for better organization.
- **Employee Management**: Manage employee information, including phone numbers and activity status.
- **User Authentication**: Secure login and registration for employees, with permissions-based access to features.
- **Search Functionality**: Search for words within the application.
- **Admin Interface**: Manage all entities (words, categories, formats, workers) via the Django admin panel.

## Demo
![Website Interface](demo.png)