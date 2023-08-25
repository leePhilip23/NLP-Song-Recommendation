from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import time # use to test loading animation

app = FastAPI()

origins = [
    "http://localhost:3000",  # Add your frontend's URL here
    "http://localhost:3001",  # Add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variable to store posted text
stored_text = ""

@app.post("/post_text/")
async def post_text(request_data: dict):
    global stored_text
    stored_text = request_data.get("text", "")
    # time.sleep(1) # use to test loading animation
    return {"summary": stored_text}
@app.get("/get_text/")
async def get_text():
    if stored_text:
        return stored_text
    else:
        return "No text available."

@app.get("/")
async def testing_endpoint():
    return "testing endpoint"
