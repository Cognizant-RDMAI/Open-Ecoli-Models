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
- Python 3.7 - 3.10.
- Required packages listed in requirements.txt.

All required Python packages are listed in the ```requirements.txt``` file. To install them:
```
pip install -r requirements.txt
```

### 4. Usage

#### Running the Advanced Model

1. **Prepare training and validation datasets**  
   Run the following notebooks in order:  
   - `EColi_data_v4_adv.ipynb` → generates the **training dataset**.  
   - `EColi_data_val_advance.ipynb` → generates the **validation dataset**.  
   **Output:** Preprocessed datasets ready for training and validation.  

2. **Train the advanced model**  
   Run `EColi_model_v4_adv.ipynb`.  
   **Output:**  
   - Trained advanced model(s).  
   - Performance metrics and training analysis (accuracy, cofusion matrices, etc.).  

3. **Validate the trained model**  
   Run `EColi_model_v4_adv_validation.ipynb`.  
   **Output:** Validation results and performance analysis on the validation dataset.  


#### Running the Light Model

1. **Prepare training dataset & train the light model**  
   Run `EColi_ALLUK_v4_light.ipynb`.  
   **Output:**  
   - Preprocessed training dataset.  
   - Trained light model(s).  
   - Performance metrics and training analysis.  

2. **Prepare validation dataset**  
   Run `EColi_data_val_light.ipynb`.  
   **Output:** Validation dataset ready for analysis.  

3. **Validate the trained model**  
   Run `EColi_model_v4_light_validation.ipynb`.  
   **Output:** Validation results and performance analysis on the validation dataset.  

For more details, refer to the README.md and example notebooks.
