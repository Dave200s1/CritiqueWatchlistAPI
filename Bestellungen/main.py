from fastapi import  FastAPI
from routers import  restaurants

app = FastAPI()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000 )