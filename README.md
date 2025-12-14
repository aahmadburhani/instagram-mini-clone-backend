# Instagram Mini Clone (Backend)

This project is a backend implementation of an Instagram-like application
built using Python and FastAPI.

I created this project to understand how real social media features work
internally, such as user authentication, post creation, likes, comments,
follow system, and feed generation.

## Technologies Used
- Python
- FastAPI
- SQLAlchemy
- SQLite (for development)
- JWT Authentication

## Features
- User signup and login
- Create posts with image URL and caption
- Like and unlike posts
- Comment on posts
- Follow and unfollow users
- Personalized feed based on followed users

## How to Run the Project

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Run the FastAPI server

```bash
uvicorn app.main:app --reload
