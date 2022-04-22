# capstone-waste-classification-management
Capstone Project: Image based Waste Segregation and Management using CNN

**DATASET LINKS**
1) WasteNet dataset (extension of TrashNet): https://drive.google.com/drive/folders/1zsOodIfqVZxb7wSpJKo1i72J6imALZbp?usp=sharing
2) Test Dataset: https://drive.google.com/drive/folders/1FZf5JgDasGTjMevuoM_nT9qp6q5k9OT-?usp=sharing

This repsitory consists of three main folders: CNN Model Training, Bin Monitoring and Model Deployment.

**1. CNN Model Training**
This folders consists of the following information:
* CNN Transfer Learning Codes of six networks
* Training Metrics Plot of Best model of each arcitecture
* Testing Codes
* Model Files Link: https://drive.google.com/drive/folders/1VTIHe-62fVEq5xzbSbObVxtVbxdN6Y3P?usp=sharing

**2. Bin Monitoring:**
* This folder consists of Node-red flow's JSON file.
* This file can be downloaded and imported in the node red software.

**3. Model Deployment**
* Streamlit GUI:
  * Download the python code
  * Install Streamlit "pip install streamlit"
  * Run the application "streamlit run deploy.py"
  
* Flask and FastAPI web application (only backend):
  * Create a new virtual environment
  * Install the libraries mentioned in requirements.txt
  * Make sure to include the .h5 model in the folder
  * Run the python code in the terminal
  * POST Request can be sent to the local host URL to send and receive response
  
* The app developed was deployed in Heroku cloud platform, thereby enabling the raspberry pi to act as a client and receive classification result from the server.
