from fastapi import  FastAPI,HTTPException
from models.movie_create import  MovieCreate
from models.movie_update import  MovieUpdate

api = FastAPI(title= 'Welcome to Critique Watchlist API !',version= '0.0.1')

#in memory Data
#Rating i out of 10
data = [
    {'movie_id':1,'title':'Avatar','year':2011,'genre':'Fantasy','watched':False,'rating':7},
    {'movie_id': 2, 'title': 'The Shawshank Redemption', 'year': 1994, 'genre': 'Drama', 'watched': True,
     'rating': 9.3},
    {'movie_id': 3, 'title': 'Inception', 'year': 2010, 'genre': 'Sci-Fi', 'watched': True, 'rating': 8.8},
    {'movie_id': 4, 'title': 'Pulp Fiction', 'year': 1994, 'genre': 'Crime', 'watched': False, 'rating': None}
]

#CRUD Methods
#Create
@api.post('/movies',response_model=dict)
def add_movie(movie: MovieCreate):
    try:
        if not data:
            new_entry_id = 1
        else:
            new_entry_id = max(item['movie_id'] for item in data) + 1

        new_entry = {
            'movie_id': new_entry_id,
            'title': movie.title,
            'year': movie.year,
            'genre': movie.genre,
            'watched': movie.watched,
            'rating': movie.rating
        }
        data.append(new_entry)
        return new_entry

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#Read
@api.get('/movies/{movie_id}')
def display_film(movie_id: int = None):
    for movie in data:
        if movie['movie_id'] == movie_id:
            return {'result: ': movie}

#Update Todo !!!
@api.put('/movies/{movie_id}')
def update_film(movie_id: int,updated_data: MovieUpdate ):
    for idx, movie in enumerate(data):
        if movie['movie_id'] == movie_id:
            # Update only provided fields
            if updated_data.title is not None:
                movie['title'] = updated_data.title
            if updated_data.year is not None:
                movie['year'] = updated_data.year
            if updated_data.genre is not None:
                movie['genre'] = updated_data.genre
            if updated_data.watched is not None:
                movie['watched'] = updated_data.watched
            if updated_data.rating is not None:
                movie['rating'] = updated_data.rating
            return {"message": "movie updated", "updated_task": movie}
        raise HTTPException(status_code=404, detail="movie not found")

#Delete
@api.delete('/movies/{movie_id}')
def delete_film(movie_id:int = None):
    for idx,movie in enumerate(data):
        if movie['movie_id'] == movie_id:
            return data.pop(idx)
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host= '0.0.0.0', port=8000)
