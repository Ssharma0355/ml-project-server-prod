from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Define the allowed origins
origins = [
    "http://localhost:3000",  # Your frontend's origin
    "https://www.myfrontendapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allow cookies to be sent with requests
    allow_methods=["*"],     # Allow all methods (GET, POST, PUT, DELETE, etc)
    allow_headers=["*"],     # Allow all headers
)

@app.get("/login")
def login():
    return {"message":"Server slow try again later"}