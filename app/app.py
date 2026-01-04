from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

# To automatically start and create database and tables when the application starts
@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

text_posts = {
    1: {"title": "Swastik's Day Out", "content": "I went to Nashik."},
    2: {"title": "Morning Coffee Thoughts", "content": "Nothing beats a strong coffee on a rainy morning."},
    3: {"title": "Late Night Debugging", "content": "Spent hours fixing a bug that was just a missing comma."},
    4: {"title": "Weekend Ride", "content": "Took the bike out for a long ride on the highway."},
    5: {"title": "New Tech Curiosity", "content": "Exploring how large language models reason internally."},
    6: {"title": "Office Chronicles", "content": "Architecture reviews can be intense but very insightful."},
    7: {"title": "Fitness Check", "content": "Started a short daily workout to stay consistent."},
    8: {"title": "Book Notes", "content": "Read a few chapters on AI risk and governance today."},
    9: {"title": "Quick Reflection", "content": "Productivity feels better when tasks are clearly scoped."},
    10: {"title": "Sunday Planning", "content": "Outlined goals and priorities for the upcoming week."}
}

# To get all post
@app.get("/posts")
def get_all_posts(limit:int = None): # pyright: ignore[reportArgumentType]
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

# To get ID specif post
@app.get("/posts/{id}")
def get_post(id:int) -> PostResponse:

    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Id is not present.")
    
    else:
        return text_posts.get(id) # type: ignore
    
# To create new post
@app.post("/posts")
def create_post(post:PostCreate) -> PostResponse:
    new_post = {"title":post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post # type: ignore