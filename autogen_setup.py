from IPython.display import Image, display
import autogen
from autogen.coding import LocalCommandLineCodeExecutor
import os

# Method 1: Using config file
print("=== Method 1: Using Config File ===")
try:
    config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST.json",
        filter_dict={"tags": ["gpt-4o"]}, # comment out to get all
    )
    print("Config loaded from file:", config_list)
except Exception as e:
    print("Error loading config from file:", e)

# Method 2: Using environment variable
print("\n=== Method 2: Using Environment Variable ===")
# Set this in your terminal: export OPENAI_API_KEY="your_openai_api_key"
config_list_env = [
    {
        "model": "gpt-4-0613",
        "api_key": os.getenv("OPENAI_API_KEY")
    }
]
print("Config from environment variable:", config_list_env)

# Method 3: Hardcoded (not recommended for production)
print("\n=== Method 3: Hardcoded (Not Recommended) ===")
config_list_hardcoded = [
    {
        "model": "gpt-4-0613",
        "api_key": "your_openai_api_key_here"  # Replace with actual key
    }
]
print("Config hardcoded:", config_list_hardcoded)

# Method 4: Using single OpenAI endpoint
print("\n=== Method 4: Single OpenAI Endpoint ===")
# When using a single openai endpoint, you can use the following:
config_list_single = [{"model": "gpt-4o", "api_key": os.getenv("OPENAI_API_KEY")}]
print("Single endpoint config:", config_list_single)

print("\n=== Setup Complete ===")
print("To use AutoGen, replace 'your_openai_api_key_here' with your actual OpenAI API key")
print("Or set the OPENAI_API_KEY environment variable") 