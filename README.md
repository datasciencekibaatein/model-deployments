# Bank Note Authentication API

FastAPI service classifying banknotes as authentic/forged using a Random Forest on the UCI Bank Note Authentication Dataset.

## Local Setup
pip install -r requirements-dev.txt

# run model_training.ipynb top to bottom to create model/classifier.joblib

uvicorn app:app --reload #docs at https://127.0.0.1:8000/docs