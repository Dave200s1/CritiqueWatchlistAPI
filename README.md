# 🎬 Critique Watchlist API
![npm bundle size (version)](https://img.shields.io/badge/version-0.0.1-darkblue)  ![npm bundle size (version)](https://img.shields.io/badge/language-python3-yellow)  ![npm bundle size (version)](https://img.shields.io/badge/framework-FastAPI-lightgreen) 

# tl;dr
A FastAPI-powered movie tracking system that lets you manage and rate films in your personal watchlist.

# Project Overview

This FastAPI-powered Critique Watchlist API demonstrates a complete backend system for managing a personal movie collection, combining SQLite database persistence with RESTful endpoint design. It enables real-time CRUD operations on film entries with rating tracking (0-10 scale) and watch status management, showcasing practical integration of database operations with Pydantic model validation. While optimized for development environments, the production-ready architecture can be extended with authentication and scaled databases for deployment.

## Features

- **Full CRUD Operations**: Create, Read, Update, Delete movies
- **Rating System**: Track ratings (0-10 scale)
- **Watch Status**: Mark movies as watched/unwatched
- **SQLite Backend**: Lightweight database persistence
- **Type Safety**: Pydantic model validation

## Setup

1. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn sqlite3

