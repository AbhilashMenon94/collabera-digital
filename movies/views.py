import json

from django.http import JsonResponse
from datetime import datetime
from enum import Enum
from collections import defaultdict

from movies.models import MovieModel


class RatingAgency(Enum):
    '''
    Define rating agencies
    '''
    IMDB = 'Internet Movie Database'
    R_TOM = 'Rotten Tomatoes'
    META_C = 'Metacritic'

def movie_list(request):
    '''
    Returns list of movies
    '''
    movie_data = []
    movies = MovieModel.objects.prefetch_related(
        'genre', 'director', 'writer', 'actors', 'language', 'country').all()

    def convert_reviews(review_data):
        data = []
        for review in review_data:
            if review['source'] == RatingAgency.IMDB.value:
                data.append({
                    'source' : review['source'],
                    'value' : f"{review['value']}/10",
                })
            elif review['source'] == RatingAgency.R_TOM.value:
                data.append({
                    'source' : review['source'],
                    'value' : f"{review['value'] * 10}%",
                })
            elif review['source'] == RatingAgency.META_C.value:
                data.append({
                    'source' : review['source'],
                    'value' : f"{int(review['value'] * 10)}/100",
                })
        return data

    # Iterate over each book and build custom JSON representation
    for movie in movies:
        genre = [genre.genre for genre in movie.genre.all()]
        director = [director.name for director in movie.director.all()]
        writer = [writer.name for writer in movie.writer.all()]
        actors = [actors.name for actors in movie.actors.all()]
        language = [language.name for language in movie.language.all()]
        country = [country.name for country in movie.country.all()]
        data = {
            'title': f"{movie.title}",
            'year': f"{movie.year}",
            'rated': f"{movie.rated}",
            "released": datetime.strptime(str(movie.released), '%Y-%m-%d').strftime("%d %b %Y"),
            "runtime": str(movie.runtime) + ' min' if movie.runtime > 0  else 'N/A',
            'genre': genre,
            'director': ', '.join(director),
            'writer': ', '.join(writer),
            'actors': ', '.join(actors),
            'plot': f"{movie.plot}",
            'language': ', '.join(language),
            'country': ', '.join(country),
            'awards': f"{movie.awards}",
            'poster': f"{movie.poster}",
            'ratings': convert_reviews(movie.ratings),
            'meta_score': f"{movie.meta_score}",
            'imdb_rating': f"{movie.imdb_rating}",
            'imdb_votes': f"{movie.imdb_votes:,}",
            'imdb_id': f"{movie.imdb_id}",
            'type': f"{movie.type}",
            'dvd': 
                datetime.strptime(str(movie.dvd), '%Y-%m-%d').strftime("%d %b %Y") if movie.dvd
                else 'N/A',
            'box_office': f"${movie.box_office:,.2f}",
            'production': f"{movie.production}",
            'website': f"{movie.website}",
            'date': f"{movie.date}",

        }

        movie_data.append(data)

    # Create a defaultdict to group objects by date
    grouped_objects = defaultdict(list)

    # Group objects by date
    for obj in movie_data:
        grouped_objects[obj['date']].append(obj)

    # Convert defaultdict to a regular dictionary
    result_dict = [{'date': date, 'movies': [{k: v for k, v in obj.items() if k != 'date'} for obj in movies]} for date, movies in grouped_objects.items()]

    # Return JSON response with pretty printed JSON
    return JsonResponse(result_dict, safe=False, json_dumps_params={'indent': 4})
