from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return {"summary": "Apples are one of the most iconic and widely enjoyed fruits, cherished for their crisp texture and sweet-tart flavor. With a diverse range of varieties available, from the classic Red Delicious to the tangy Granny Smith, there's an apple to suit every palate. These fruit gems are not only delicious but also packed with nutritional benefits. Apples are a great source of dietary fiber, vitamins, and antioxidants, making them a wholesome choice for maintaining a healthy lifestyle. Whether enjoyed as a quick snack, sliced into salads, or baked into pies, the versatility of apples knows no bounds. From orchards to kitchen tables, apples remain a symbol of freshness, vitality, and culinary delight."}

@app.get("/get_text/")
async def get_text():
    if stored_text:
        return stored_text
    else:
        return "No text available."

@app.get("/")
async def testing_endpoint():
    return "testing endpoint"
