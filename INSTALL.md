Installation Guide
This guide walks you through setting up the **Open E. Coli Model** project in your local or cloud environment.
 

--- 
## Installation Instructions
### 1. Clone the repository
 
First, clone this project to your local machine or cloud environment:
```
git clone  <repository_url>  cd ai-ecoli-model
```
This will download all project files including the model scripts.

*Note:* Adjust the data paths according to your local environment.

 
### 2. Create a Python Virtual Environment (Optional but Recommended)
 
Using a virtual environment avoids conflicts with other Python packages on your system
```
python3 -m venv venv
source venv/bin/activate    #macOS/Linux
venv/Scripts/Activate       #Windows
```
This creates an isolated environment where all dependencies will be installed.

### 3. Install Dependencies

Prerequisites:
- Python 3.7 or higher.
- Required packages listed in requirements.txt.

All required Python packages are listed in the ```requirements.txt``` file. To install them:
```
pip install -r requirements.txt
```

For more details, refer to the README.md and example notebooks.