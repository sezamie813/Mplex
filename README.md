# 🚀 TerminalForge

**AI-Powered Development Environment** - Transform your terminal into an intelligent development powerhouse!

TerminalForge combines FastAPI, Moulti TUI, and Google Gemini AI to create complete applications from simple descriptions. Watch as AI generates entire project structures, writes code, creates tests, and handles deployment - all displayed in beautiful, interactive terminal interfaces.

![TerminalForge Demo](docs/assets/demo.gif)

## ✨ Features

- **🤖 AI-Powered Code Generation** - Generate entire applications from descriptions
- **📺 Interactive TUI** - Beautiful Moulti-powered terminal interface
- **⚡ FastAPI Backend** - Robust API for managing projects and AI operations
- **🧪 Automated Testing** - AI generates and runs comprehensive tests
- **🐳 Docker Integration** - Automatic containerization and deployment
- **📁 Smart Project Templates** - Industry-standard project structures
- **🔧 CLI-First Design** - Everything accessible from the command line

## 🎯 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/terminalforge.git
cd terminalforge

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your Gemini API key

# Install CLI tool
pip install -e .
```

### Create Your First Project

```bash
# Generate a complete FastAPI CRUD app
terminalforge create "Build me a FastAPI CRUD app for managing books with PostgreSQL and Redis caching"

# Or interactively
terminalforge create --interactive
```

Watch as TerminalForge:
1. **Analyzes** your requirements using Gemini AI
2. **Generates** the complete project structure
3. **Writes** all the code files
4. **Creates** database models and migrations
5. **Sets up** Docker configuration
6. **Generates** comprehensive tests
7. **Displays** everything in a beautiful TUI

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    TerminalForge CLI                      │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                  FastAPI Backend                          │
│  ┌─────────────┐ ┌──────────────┐ ┌──────────────────┐ │
│  │   Projects  │ │  AI Service  │ │  Code Generator  │ │
│  │   Manager   │ │              │ │                  │ │
│  └─────────────┘ └──────────────┘ └──────────────────┘ │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                  Moulti TUI                              │
│  ┌─────────────┐ ┌──────────────┐ ┌──────────────────┐ │
│  │   Step 1    │ │    Step 2    │ │     Step 3       │ │
│  │  Project    │ │  Code Gen    │ │    Testing       │ │
│  │   Setup     │ │              │ │                  │ │
│  └─────────────┘ └──────────────┘ └──────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Core Components

### FastAPI Backend (`terminalforge/api/`)
- **Project Management**: Create, manage, and track projects
- **AI Integration**: Gemini-powered code generation and analysis
- **File Operations**: Intelligent file system management
- **Git Integration**: Automated version control operations

### Moulti TUI (`terminalforge/moulti_integration/`)
- **Step Management**: Visual progress tracking
- **Real-time Updates**: Live output streaming
- **Interactive Controls**: User input and decision points
- **Progress Tracking**: Visual progress indicators

### AI Services (`terminalforge/services/`)
- **Code Generation**: Intelligent code creation
- **Test Creation**: Automated test generation
- **Code Analysis**: Quality and security analysis
- **Documentation**: Auto-generated documentation

## 🎯 Use Cases

### 1. Rapid Prototyping
```bash
terminalforge create "Build a REST API for a customer management system with JWT authentication"
```

### 2. Code Generation
```bash
terminalforge generate code --prompt "Create a Python function to validate email addresses with regex"
```

### 3. Test Automation
```bash
terminalforge generate tests --path ./src/auth.py
```

### 4. Project Analysis
```bash
terminalforge analyze --path ./project --focus performance,security
```

### 5. Deployment
```bash
terminalforge deploy --env production --strategy docker
```

## 🔧 Configuration

### Environment Variables
```bash
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional
MOULTI_INSTANCE=terminalforge
LOG_LEVEL=INFO
PROJECTS_DIR=./projects
```

### CLI Configuration
```yaml
# ~/.terminalforge/config.yaml
default_model: gemini-2.0-flash
output_format: json
projects_dir: ~/terminalforge-projects
templates:
  - fastapi-crud
  - django-api
  - react-app
  - nodejs-api
```

## 🚀 Advanced Usage

### Custom Templates
Create your own project templates:

```python
# templates/my_template.py.j2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class {{ model_name }}(BaseModel):
    {% for field in fields %}
    {{ field.name }}: {{ field.type }}
    {% endfor %}

@app.{{ method }}("/{{ endpoint }}")
async def {{ function_name }}():
    # Generated code here
    pass
```

### Batch Processing
```bash
# Process multiple projects
terminalforge batch --input projects.txt --output results.json

# Generate from file
terminalforge create --file project_description.md
```

### Integration
```python
# Integrate with CI/CD
import terminalforge

project = terminalforge.create_project(
    description="Build authentication service",
    template="fastapi-auth",
    config={
        "database": "postgresql",
        "cache": "redis",
        "auth": "jwt"
    }
)

terminalforge.generate_tests(project)
terminalforge.deploy(project, environment="staging")
```

## 📊 Examples

### Book Management System
```bash
terminalforge create "Build a FastAPI application for managing books with:
- CRUD operations for books and authors
- PostgreSQL database with SQLAlchemy
- Redis caching for performance
- JWT authentication
- Role-based access control (admin, user)
- Search and filtering
- Pagination
- Docker support
- Comprehensive tests"
```

### E-commerce API
```bash
terminalforge create "Create a complete e-commerce REST API with:
- Product catalog management
- Shopping cart functionality
- Order processing
- Payment integration (Stripe)
- User authentication
- Admin dashboard
- Inventory tracking
- Email notifications
- Background job processing
- API documentation"
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run specific test suite
pytest tests/test_services/

# Run with coverage
pytest --cov=terminalforge tests/

# Integration tests
pytest tests/integration/
```

## 📝 Development

```bash
# Set up development environment
make dev-setup

# Run development server
make dev

# Run linting
make lint

# Run type checking
make type-check

# Build documentation
make docs
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The modern, fast web framework
- [Moulti](https://moulti.run/) - The brilliant CLI-driven TUI
- [Google Gemini](https://ai.google.dev/) - The powerful AI model
- [Textual](https://textual.textualize.io/) - The TUI framework powering Moulti

## 📞 Support

- 📧 Email: support@terminalforge.dev
- 💬 Discord: [Join our server](https://discord.gg/terminalforge)
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/terminalforge/issues)

---

**Made with ❤️ by the TerminalForge Team**
