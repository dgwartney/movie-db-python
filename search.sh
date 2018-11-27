#!/bin/bash
curl --request GET --url "https://api.themoviedb.org/3/search/movie?api_key=${MOVIE_DB_API_KEY}&query=Jack+Reacher" #--header 'Content-Type: application/json;charset=utf-8'
