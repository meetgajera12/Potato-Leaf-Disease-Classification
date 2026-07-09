from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

MODEL = tf.keras.models.load_model(r"Potato-dieses\my_model.keras")
CLASS_NAME = ['Early Blight', 'Late Blight', 'Healthy']

@app.get("/ping")
async def ping():
    return "hello, i am here!"


def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    image = image.resize((256, 256))
    image = np.array(image)
    return image 

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    
    image_batch = np.expand_dims(image,0)

    prediction = MODEL.predict(image_batch)

    predicted_class = CLASS_NAME[np.argmax(prediction[0])]

    confidence = float(np.max(prediction[0]))

    # print(prediction)
    # print(np.argmax(prediction[0]))

    return {"class" : predicted_class, 'confidence' : confidence}
    


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
