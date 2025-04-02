from fastapi import  FastAPI
from routers import  restaurants

app = FastAPI(title="Restaurant API", version="0.1.0")

app.include_router(restaurants.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Restaurant API"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000 )