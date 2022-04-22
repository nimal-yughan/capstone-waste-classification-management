from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()
model = tf.keras.models.load_model("vgg16_b32_f.h5")

def read_image(image_encoded) -> Image.Image:
    pil_image=Image.open(BytesIO(image_encoded))
    return pil_image

def predict_class(image: Image.Image):
    #img=Image.open(file_path)
    img = image.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array2 = tf.keras.applications.vgg16.preprocess_input(img_array)
    img_array2 = tf.expand_dims(img_array2, 0)
    result = model.predict(img_array2)
    class_subset = ['cardboard', 'ewaste', 'glass', 'metal', 'organic', 'paper', 'plastic']
    predicted_class = class_subset[np.argmax(result[0])]
    return predicted_class

@app.get("/ping")
async def ping():
    return "It is working"

@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    image = read_image(await file.read())
    result = predict_class(image)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)


