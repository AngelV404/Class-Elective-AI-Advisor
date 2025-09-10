# Class-Elective-AI-Advisor
This application is an AI-powered application designed to streamline the course selection process for university students by providing personalized elective and mandatory course recommendations. The system integrates OpenAi’s ChatGPT API  to analyze students preferences, academic goals, and career aspirations to deliver tailored  suggestions.

---

## Prerequisites

- Python 3.10 or higher installed
- `pip` installed (usually comes with Python)
- On Windows: Python added to your PATH
- On Linux: `python3-tk` installed for Tkinter GUI support (see below)

---

## Tools and Dependencies

The project requires the following tools and libraries:

- **Python 3.10+** – main programming language
- **pip** – Python package manager
- **Tkinter (`python3-tk`)** – GUI library for Linux
- **SQLite** – lightweight database for storing user and course data
- **AWS SDK / boto3** – for authentication or other AWS integrations
- **OpenAI API** – for LLM/ChatGPT integration
- **LangGraph** – pipeline for LLM management

---

## Setup Instructions

### Windows
1. Open Command Prompt (or PowerShell).  
2. Navigate to the project folder where `setup.bat` is located.  
3. Run the setup script:

```cmd
setup.bat
```

4. After completion, activate the virtual environment manually (if needed):

```cmd
venv\Scripts\activate.bat
```

### Linux / WSL / macOS

1. Open Terminal.
2. Navigate to the project folder where `setup.sh` is located.
3. Make the script executable (only first time):

```bash
chmod +x setup.sh
```

4. Install Tkinter (if not already installed):

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

5. Run the setup script:

```bash
./setup.sh
```

6. Activate the virtual environment (if not automatically activated):

```bash
source venv/bin/activate
```

---