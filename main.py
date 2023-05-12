import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List, Optional
from pydantic import BaseModel, EmailStr

app = FastAPI()

#@app.get("/")
#async def index():
   #return {"message": "Bonjuor"}
#if __name__ == "__main__":
   #uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

#@app.get("/users/{user_id}")
#async def user(user_id: str):
    #return {"user_id":user_id}
#if __name__ == "__main__":
   #uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

#userlist = ["Spike","Jet","Ed","Faye","Ein"]

#@app.get("/userlist")
#async def userlist_(start: int = 0, limit: int = 10):
    #return userlist[start:start+limit]
#if __name__ == "__main__":
   #uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

### Response Types in FastAPI

#@app.get("/")
#async def index():
   #return HTMLResponse("<h1>Hello Sri Lanka</h1>")
#if __name__ == "__main__":
   #uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


### Using Pydantic models with FastAPI

class Movie(BaseModel):
    name: str
    year: int
    rating: Optional[int] = None
    tags: List[str] = []

@app.post("/movies/", response_model=Movie)
async def create_movie(movie: Movie):
    return movie
if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

