# AutoGen Setup Guide

This project demonstrates how to set up AutoGen with different OpenAI API key configuration methods.

## Prerequisites

1. Install required packages:
```bash
pip3 install autogen-agentchat~=0.2 matplotlib yfinance
```

2. Get an OpenAI API key from https://platform.openai.com/api-keys

## API Key Configuration Methods

### Method 1: Environment Variable (Recommended)

**Linux/MacOS:**
```bash
export OPENAI_API_KEY="your_openai_api_key"
```

**Windows:**
```cmd
set OPENAI_API_KEY=your_openai_api_key_here
```

### Method 2: Config File

Edit `OAI_CONFIG_LIST.json` and replace `"your_openai_api_key_here"` with your actual API key.

### Method 3: Hardcoded (Not Recommended for Production)

Edit `autogen_setup.py` and replace the placeholder with your actual API key.

## Usage

Run the setup script to test your configuration:

```bash
python3 autogen_setup.py
```

## Files

- `autogen_setup.py` - Main script demonstrating different configuration methods
- `OAI_CONFIG_LIST.json` - Configuration file for API settings
- `hello.py` - Original Git lab file
- `README.md` - This file

## Security Notes

- Never commit your actual API key to version control
- Use environment variables for production applications
- The `OAI_CONFIG_LIST.json` file is included in `.gitignore` to prevent accidental commits 