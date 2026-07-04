# 🥔 Potato Leaf Disease Classification

A Deep Learning project that classifies potato leaf diseases using Convolutional Neural Networks (CNN) with Data Augmentation.

The application consists of:

- 🚀 FastAPI backend for model inference
- 🎨 Streamlit frontend for user interaction
- 🧠 TensorFlow/Keras CNN model
- 📈 Data Augmentation for improved generalization

---

## Demo

### Workflow

```text
Upload Image
↓
Streamlit Frontend
↓
FastAPI Backend
↓
CNN Model (.keras)
↓
Prediction Result
```

---

## Dataset

Dataset contains potato leaf images belonging to three classes:

- Potato Early Blight
- Potato Late Blight
- Potato Healthy

> Dataset used for training is not included because of its large size. (but zip file is provided.)

---

## Project Structure

```text
Potato-Leaf-Disease-Classification
│
├── api/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── training.ipynb
├── img_Classification_with_DataAugmentation.ipynb
├── my_model.keras
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Technologies Used

- Python
- TensorFlow
- Keras
- FastAPI
- Streamlit
- NumPy
- Pillow

---

## Model Training

The model was trained using:

- CNN Architecture
- ImageDataGenerator
- Data Augmentation
- Adam Optimizer
- Categorical Crossentropy Loss

---

## Installation

Clone the repository

```bash
git clone https://github.com/meetgajera12/Potato-Leaf-Disease-Classification.git

cd Potato-Leaf-Disease-Classification
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI Backend

```bash
cd api

uvicorn main:app --reload
```

Runs on

```
http://127.0.0.1:8000
```

---

## Run Streamlit Frontend

Open another terminal

```bash
cd frontend

streamlit run app.py
```

---

## API Endpoint

### POST `/predict`

Accepts an image file and returns:

```json
{
    "class": "Potato___Late_Blight",
    "confidence": 98.74
}
```

---

## Future Improvements

- Improve model accuracy
- Support multiple crop diseases
- Model Versioning
- Docker Support

---

## Author

***Meet Gajera***

AI & Data Science Student

GitHub:
https://github.com/meetgajera12
