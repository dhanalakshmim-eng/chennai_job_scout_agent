import os
from dotenv import load_dotenv

print(f"--- Diagnostic Report ---")
print(f"Current Directory: {os.getcwd()}")

# Look for the file manually
if os.path.exists(".env"):
    print("✅ Found .env file!")
    with open(".env", "r") as f:
        first_line = f.readline()
        if "GROQ_API_KEY" in first_line:
            print("✅ Key variable name found in file.")
        else:
            print("❌ GROQ_API_KEY name NOT found in file. Check spelling.")
else:
    print("❌ No .env file found in this folder.")
    print(f"Files found here: {os.listdir('.')}")

# Try to load it
load_dotenv()
key = os.getenv("GROQ_API_KEY")

if key:
    print(f"✅ Key loaded into memory! (Ends with: ...{key[-4:]})")
else:
    print("❌ load_dotenv() failed to push key into os.environ.")