# VS Code Setup Guide for 100xJobs Django Project

This guide will help you set up VS Code for optimal Django development with the 100xJobs project.

## 🚀 Quick Setup

### 1. Open Project in VS Code
```bash
cd /Users/soubhagyaghoshal/Downloads/Job
code .
```

### 2. Copy Configuration Files
```bash
# Copy the example files to create your personal settings
cp .vscode/settings.json.example .vscode/settings.json
cp .vscode/launch.json.example .vscode/launch.json
```

### 3. Select Python Interpreter
1. Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
2. Type "Python: Select Interpreter"
3. Choose `./venv/bin/python` (the virtual environment)

## 📦 Recommended Extensions

VS Code will automatically suggest these extensions when you open the project:

### Essential Extensions
- **Python** - Python language support
- **Django** - Django template syntax highlighting
- **Pylint** - Python linting
- **Black Formatter** - Code formatting
- **isort** - Import sorting

### Helpful Extensions
- **Auto Rename Tag** - Automatically rename paired HTML tags
- **Path Intellisense** - Autocomplete filenames
- **GitLens** - Enhanced Git capabilities
- **Tailwind CSS IntelliSense** - For CSS classes

## 🏃‍♂️ Running the Project

### Method 1: Using Debug Panel (Recommended)
1. Go to the Debug panel (`Cmd+Shift+D`)
2. Select "Django: Run Server" from the dropdown
3. Click the green play button
4. Server will start at http://127.0.0.1:8000

### Method 2: Using Tasks
1. Press `Cmd+Shift+P`
2. Type "Tasks: Run Task"
3. Select "Django: Run Server"

### Method 3: Using Terminal
1. Open integrated terminal (`Cmd+` ` or `Ctrl+` `)
2. Run: `source venv/bin/activate && python manage.py runserver`

## 🐛 Debugging

### Set Breakpoints
1. Click in the left margin of any Python file to set breakpoints
2. Use "Django: Debug Server" configuration
3. Debug panel will show variables, call stack, etc.

### Debug Configurations Available
- **Django: Run Server** - Normal server run
- **Django: Debug Server** - Server with debugging enabled
- **Django: Test** - Run Django tests
- **Django: Shell** - Django interactive shell
- **Django: Migrate** - Run database migrations

## ⚙️ Available Tasks

Access via `Cmd+Shift+P` → "Tasks: Run Task":

- **Django: Run Server** - Start development server
- **Django: Make Migrations** - Create new migrations
- **Django: Migrate** - Apply migrations
- **Django: Create Superuser** - Create admin user
- **Django: Collect Static** - Collect static files
- **Install Requirements** - Install Python dependencies

## 🔧 Key Features Configured

### Code Quality
- **Auto-formatting** with Black on save
- **Import sorting** with isort
- **Linting** with Flake8
- **Type checking** support

### Django-Specific
- **Template syntax highlighting** for Django templates
- **Model and view navigation**
- **Django command integration**
- **Environment variable support**

### File Management
- **Hidden files**: `__pycache__`, `*.pyc`, `venv/`, etc.
- **Search exclusions**: Virtual env and cache directories
- **Auto file associations**: HTML, CSS, JS

## 🌐 Browser Integration

### Live Server
The debug configuration will automatically start the server at:
- **Local**: http://127.0.0.1:8000
- **Admin**: http://127.0.0.1:8000/admin/

### Test Accounts
- **Admin**: admin / admin123
- **Employer**: employer1 / password123
- **Job Seeker**: jobseeker1 / password123

## 📁 Project Structure in VS Code

```
100xJobs/
├── .vscode/                 # VS Code configuration
│   ├── settings.json        # Editor settings
│   ├── launch.json          # Debug configurations
│   ├── tasks.json           # Task definitions
│   └── extensions.json      # Recommended extensions
├── jobportal/               # Django project settings
├── jobs/                    # Jobs app
├── accounts/                # User accounts app
├── templates/               # HTML templates
├── static/                  # Static files (CSS, JS, images)
├── venv/                    # Virtual environment
├── manage.py                # Django management script
└── requirements.txt         # Python dependencies
```

## 🚨 Troubleshooting

### Python Interpreter Not Found
1. Ensure virtual environment is created: `python -m venv venv`
2. Activate it: `source venv/bin/activate`
3. Install requirements: `pip install -r requirements.txt`
4. Restart VS Code and select interpreter again

### Django Server Won't Start
1. Check if virtual environment is activated
2. Ensure all dependencies are installed
3. Run migrations: `python manage.py migrate`
4. Check for port conflicts (kill other processes on port 8000)

### Extensions Not Working
1. Install recommended extensions from the Extensions panel
2. Reload VS Code window (`Cmd+R`)
3. Check Python interpreter is correctly selected

## 💡 Pro Tips

### Keyboard Shortcuts
- `Cmd+Shift+P` - Command palette
- `Cmd+` ` - Toggle terminal
- `Cmd+Shift+D` - Debug panel
- `F5` - Start debugging
- `Cmd+F5` - Run without debugging

### Django-Specific Tips
1. Use `Cmd+Click` to navigate to Django models/views
2. Set breakpoints in views for debugging requests
3. Use Django shell for testing: Select "Django: Shell" debug config
4. Monitor server logs in the integrated terminal

### Git Integration
- VS Code has built-in Git support
- Use GitLens extension for enhanced features
- Commit changes directly from VS Code
- View file history and blame information

## 🔄 Development Workflow

1. **Start**: Open project in VS Code
2. **Code**: Edit files with auto-completion and linting
3. **Test**: Run server with debugging enabled
4. **Debug**: Set breakpoints and inspect variables
5. **Commit**: Use integrated Git features
6. **Deploy**: Push to GitHub (auto-deploys to Vercel)

This setup provides a professional Django development environment with all the tools you need for efficient coding, debugging, and deployment!
