# Multilingual FAQ System

A Django-based FAQ management system with multilingual support and WYSIWYG editing.

## Features

- Multi-language support (EN, HI, BN)
- WYSIWYG editor for answers
- Automatic translation
- Caching for performance
- RESTful API

## Installation

```bash
git clone <repository-url>
cd faq_system
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

## API Usage

```bash
# Get FAQs in English
GET /api/faqs/

# Get FAQs in Hindi
GET /api/faqs/?lang=hi

# Get FAQs in Bengali
GET /api/faqs/?lang=bn
```

## Testing and Code Quality

Run tests:

```bash
# Run all tests
python manage.py test

# Run with coverage report
coverage run manage.py test
coverage report

# Check code style
flake8 .
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## Tech Stack

- Django
- Django REST Framework
- CKEditor
- Google Translate API
- Redis (optional)
```
