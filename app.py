import numpy as np
import cv2
from fastapi import FastAPI, File, UploadFile
import uvicorn

from services.image_processing import get_contours_text_image
from services.text_processing import get_texts

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World2"}


@app.post("/accounts")
async def read_item(file: UploadFile = File(...)):
    contents = await file.read()
    np_arr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        contours = get_contours_text_image(img)
        return get_texts(img, contours)
        

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,log_level="info")
