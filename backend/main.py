import uvicorn
from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # @todo set production origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/text")
def generate_image():

    response = requests.get("https://baconipsum.com/api/?type=meat-and-filler")
    return response.text

if __name__=="__main__":
    uvicorn.run("main:app",host='0.0.0.0', port=4557, reload=True, workers=3)

