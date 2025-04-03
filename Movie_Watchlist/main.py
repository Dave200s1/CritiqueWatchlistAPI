from fastapi import  FastAPI,HTTPException
from models.movie_create import  MovieCreate
from models.movie_update import  MovieUpdate
import sqlite3
from contextlib import closing


api = FastAPI(title= 'Welcome to Critique Watchlist API !',version= '0.0.1')

#in memory Data
#Rating i out of 10

def get_db():
    return  sqlite3.connect('data.db')

def row_to_dict(row):
    return dict(zip([col[0] for col in row.description], row))

#CRUD Methods
#Create
@api.post('/movies', response_model=dict)
def add_movie(movie: MovieCreate):
    try:
        with closing(get_db()) as db:
            cursor = db.cursor()
            cursor.execute('''
                INSERT INTO movies (title, year, genre, watched, rating)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                movie.title,
                movie.year,
                movie.genre,
                int(movie.watched),  # Convert bool to int for SQLite
                movie.rating
            ))
            db.commit()


            new_id = cursor.lastrowid
            return {
                "movie_id": new_id,
                "title": movie.title,
                "year": movie.year,
                "genre": movie.genre,
                "watched": movie.watched,
                "rating": movie.rating
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@api.get('/movies/{movie_id}')
def display_film(movie_id: int):
    with closing(get_db()) as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute('''
            SELECT * FROM movies WHERE movie_id = ?
        ''', (movie_id,))
        movie = cursor.fetchone()

        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")


        movie_dict = dict(movie)
        movie_dict['watched'] = bool(movie_dict['watched'])  # Convert int back to bool
        return movie_dict


@api.put('/movies/{movie_id}')
def update_film(movie_id: int, updated_data: MovieUpdate):
    try:
        with closing(get_db()) as db:
            db.row_factory = sqlite3.Row
            update_fields = updated_data.dict(exclude_unset=True)

            if not update_fields:
                raise HTTPException(status_code=400, detail="No fields to update")


            if 'watched' in update_fields:
                update_fields['watched'] = int(update_fields['watched'])

            set_clause = ", ".join([f"{key} = ?" for key in update_fields.keys()])
            values = list(update_fields.values())
            values.append(movie_id)

            cursor = db.cursor()
            cursor.execute(f'''
                UPDATE movies 
                SET {set_clause}
                WHERE movie_id = ?
            ''', values)

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Movie not found")

            db.commit()


            cursor.execute('SELECT * FROM movies WHERE movie_id = ?', (movie_id,))
            updated_movie = cursor.fetchone()
            movie_dict = dict(updated_movie)
            movie_dict['watched'] = bool(movie_dict['watched'])

            return {"message": "Movie updated", "updated_movie": movie_dict}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@api.delete('/movies/{movie_id}')
def delete_film(movie_id: int):
    with closing(get_db()) as db:
        cursor = db.cursor()
        cursor.execute('DELETE FROM movies WHERE movie_id = ?', (movie_id,))

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Movie not found")

        db.commit()
        return {"message": "Movie deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host= '0.0.0.0', port=8000)
