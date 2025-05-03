# SEC E-commerce Project

**Created by**:
1) Priyongshu Paul - BA English (Honours) - 24/40525
2) Abhay Pratap Singh - BA English (Honours)



## Features

- **Product Management**
  - Create, update, and delete products
  - Product categorization
  - Image upload support
  - Detailed product descriptions
  - Price management
  - Availability tracking


- **Category System**
  - Hierarchical category organization
  - SEO-friendly URLs
  - Category-specific product filtering

- **User Interface**
  - Responsive design
  - Product detail pages
  - Category browsing
  - Clean and intuitive navigation

## Project Structure

```
SEC_ecommerce_project/
├── store/                      # Main application directory
│   ├── admin.py               # Admin interface configuration
│   ├── apps.py                # App configuration
│   ├── models.py              # Database models
│   ├── views.py               # View logic
│   ├── urls.py                # URL routing
│   ├── tests.py               # Test cases
│   ├── static/                # Static files (CSS, JS, images)
│   ├── templates/             # HTML templates
│   └── migrations/            # Database migrations
├── ecommerce_project/         # Project settings
├── media/                     # User-uploaded media files
├── db.sqlite3                 # Database file
└── manage.py                  # Django management script
```

## Technology Stack

- **Backend**: Django
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Media Storage**: Local file system

## Getting Started

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
## Pictures

**Frontend**

![front1](/assets/SCR-20250503-rxqd.jpeg)

![front2](/assets/SCR-20250503-rxrd.png)

![front1](/assets/SCR-20250503-rxsj.png)

**Backend**

![back1](/assets/SCR-20250503-sayk.png)

![back2](/assets/SCR-20250503-sazr.png)


## License

This project is licensed under the MIT License - see the LICENSE file for details. 