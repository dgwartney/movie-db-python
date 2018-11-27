#!/usr/bin/env python
import tmdbsimple as tmdb
import os
tmdb.API_KEY = os.environ['MOVIE_DB_API_KEY']

movie = tmdb.Movies(603)
response = movie.info()
response = movie.releases()
for c in movie.countries:
    if c['iso_3166_1'] == 'US':
        print(c['certification'])

search = tmdb.Search()
response = search.movie(query='The Bourne')
for s in search.results:
    print(s['title'], s['id'], s['release_date'], s['popularity'])
