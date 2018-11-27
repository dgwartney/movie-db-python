#!/bin/bash
curl --request GET --url "https://api.themoviedb.org/4/list/1?page=1,&api_key=${MOVIE_DB_API_KEY}" --header 'Content-Type: application/json;charset=utf-8'
