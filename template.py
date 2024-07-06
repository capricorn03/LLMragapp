import os 
from pathlib import Path


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "app.py",
    "requirements.txt",
    "demo.py",
    "setup.py",
    "research/trials.ipynb",
    
]
 
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")