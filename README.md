# 🎯 Django CV PDF Generator

A modern Django web application that allows users to create professional CVs (Curriculum Vitae) with multiple education entries and generate downloadable PDFs. This project demonstrates Django formsets, PDF generation, and modern UI design.

## ✨ Features

- **📝 Dynamic CV Creation**: Create professional CVs with personal information, education, work experience, and skills
- **🎓 Multiple Education Entries**: Add unlimited education entries with degree, university, graduation year, GPA, and descriptions
- **📄 PDF Generation**: Generate professional PDFs using `pdfkit` and `wkhtmltopdf`
- **🎨 Modern UI**: Beautiful, responsive design with Bootstrap 5 and custom CSS
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **🔧 Debug Tools**: Built-in debugging tools for PDF generation issues

## 🛠️ Technologies Used

- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **PDF Generation**: `pdfkit`, `wkhtmltopdf`
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter)
- **Database**: SQLite (default) / PostgreSQL / MySQL
- **IDE**: Cursor IDE (AI-powered code editor)

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- pip (Python package installer)
- Git
- wkhtmltopdf (for PDF generation)
- Cursor IDE (recommended for development)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-cv-pdf-generator.git
cd django-cv-pdf-generator
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install wkhtmltopdf

#### Windows:
1. Download from [wkhtmltopdf Downloads](https://wkhtmltopdf.org/downloads.html)
2. Install to default location (`C:\Program Files\wkhtmltopdf\`)
3. Add to PATH (optional)

#### macOS:
```bash
brew install wkhtmltopdf
```

#### Ubuntu/Debian:
```bash
sudo apt-get install wkhtmltopdf
```

### 5. Run Migrations

```bash
cd mysite
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the application.

## 💻 Development Environment

This project was developed using **Cursor IDE**, an AI-powered code editor that significantly enhanced the development experience. Cursor IDE provided:

- **AI Code Assistance**: Intelligent code completion and suggestions
- **Real-time Error Detection**: Immediate feedback on syntax and logic errors
- **Smart Refactoring**: AI-powered code optimization and restructuring
- **Context-Aware Help**: Relevant documentation and examples based on current code
- **Integrated Terminal**: Built-in terminal for running Django commands
- **Git Integration**: Seamless version control with Git

### Why Cursor IDE?

Cursor IDE was chosen for this project because it:
- Accelerates Django development with AI assistance
- Provides intelligent suggestions for Django patterns and best practices
- Helps with debugging and troubleshooting
- Offers excellent support for Python and web technologies
- Enhances productivity through AI-powered code generation

**Download Cursor IDE**: [https://cursor.sh/](https://cursor.sh/)

## 📁 Project Structure

```
django-cv-pdf-generator/
├── mysite/                          # Django project root
│   ├── manage.py                    # Django management script
│   ├── mysite/                      # Project settings
│   │   ├── __init__.py
│   │   ├── settings.py              # Django settings
│   │   ├── urls.py                  # Main URL configuration
│   │   └── wsgi.py
│   ├── pdf/                         # Main app
│   │   ├── __init__.py
│   │   ├── admin.py                 # Django admin configuration
│   │   ├── apps.py                  # App configuration
│   │   ├── forms.py                 # Django forms and formsets
│   │   ├── models.py                # Database models
│   │   ├── urls.py                  # App URL patterns
│   │   ├── views.py                 # Django views
│   │   └── templates/               # HTML templates
│   │       └── pdf/
│   │           ├── profile_form.html    # CV creation form
│   │           └── profile_detail.html  # CV display and PDF generation
│   └── db.sqlite3                   # SQLite database
├── requirements.txt                 # Python dependencies
├── INSTALLATION_GUIDE.md           # wkhtmltopdf installation guide
└── README.md                       # This file
```

## 🗄️ Database Models

### ProfileModel
- `name`: Full name of the person
- `email`: Email address
- `phone`: Phone number
- `summary`: Professional summary
- `previous_work`: Work experience
- `skills`: Skills and competencies

### Education
- `profile`: Foreign key to ProfileModel
- `degree`: Degree or qualification
- `university`: University or institution name
- `graduation_year`: Year of graduation
- `gpa`: Grade Point Average
- `description`: Additional education details
- `order`: Ordering field

## 🎯 Key Features Explained

### 1. Dynamic Education Formsets

The project uses Django formsets to handle multiple education entries:

```python
# forms.py
EducationFormSet = forms.inlineformset_factory(
    ProfileModel,
    Education,
    form=EducationForm,
    extra=1,
    can_delete=True,
    fields=['degree', 'university', 'graduation_year', 'gpa', 'description']
)
```

### 2. PDF Generation

Two methods for PDF generation:

- **Primary Method**: `generate_pdf()` - Uses `pdfkit.from_string()`
- **Alternative Method**: `generate_pdf_alternative()` - Uses `pdfkit.from_file()` with temporary files

### 3. Modern UI Design

- Responsive design with Bootstrap 5
- Custom CSS with gradients and modern styling
- Font Awesome icons
- Professional color scheme

## 🔧 Usage

### Creating a CV

1. Visit `http://127.0.0.1:8000/profile/create/`
2. Fill in personal information
3. Add education entries using "Add Another Education" button
4. Fill in work experience and skills
5. Click "Generate My CV"

### Viewing and Downloading CV

1. View the generated CV at the detail page
2. Use "Generate PDF" button for primary PDF generation
3. Use "Download PDF" button for alternative PDF generation
4. Use "Debug" button to troubleshoot PDF generation issues

## 🐛 Troubleshooting

### Common Issues

#### 1. "No wkhtmltopdf executable found"
- Ensure wkhtmltopdf is installed
- Check installation paths in `views.py`
- Add wkhtmltopdf to system PATH

#### 2. PDF Generation Fails
- Check wkhtmltopdf installation
- Verify file permissions
- Use debug button to check configuration

#### 3. Form Errors
- Ensure all required fields are filled
- Check form validation in browser console

### Debug Tools

The project includes a debug view (`/profile/<id>/debug-pdf/`) that shows:
- wkhtmltopdf installation status
- Version information
- Path configuration
- System information

## 🎨 Customization

### Styling

Modify `mysite/pdf/templates/pdf/profile_detail.html` to customize:
- Colors and gradients
- Typography
- Layout and spacing
- Print styles

### Adding New Fields

1. Update models in `models.py`
2. Run migrations
3. Update forms in `forms.py`
4. Modify templates
5. Update views if needed

### PDF Options

Customize PDF generation options in `views.py`:

```python
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    # Add more options as needed
}
```

## 📚 Learning Resources

This project demonstrates several Django concepts:

- **Class-Based Views**: `CreateView`, `DetailView`
- **Formsets**: `inlineformset_factory` for related models
- **Template Inheritance**: Base templates and blocks
- **Static Files**: CSS, JavaScript, and external libraries
- **URL Patterns**: Named URLs and reverse lookups
- **Model Relationships**: Foreign keys and related names
- **PDF Generation**: External library integration

### 🚀 Development Tips with Cursor IDE

When working on this project with Cursor IDE:

1. **Use AI Chat**: Ask Cursor for help with Django patterns, debugging, or code optimization
2. **Leverage Auto-completion**: Cursor's AI can suggest Django-specific code patterns
3. **Quick Refactoring**: Use Cursor's AI to refactor code and improve structure
4. **Error Resolution**: Cursor can help identify and fix common Django errors
5. **Code Documentation**: Ask Cursor to generate comments and documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Django community for the excellent framework
- wkhtmltopdf team for PDF generation capabilities
- Bootstrap team for the responsive CSS framework
- Font Awesome for the beautiful icons
- Cursor IDE team for the AI-powered development experience

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section
2. Use the debug tools in the application
3. Open an issue on GitHub
4. Check the Django documentation

---

**Happy Coding! 🚀**

This project is perfect for Django beginners to learn:
- Model relationships and formsets
- PDF generation with external libraries
- Modern UI design with CSS
- Template rendering and context
- URL routing and views
- Form handling and validation 