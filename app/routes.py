from app import app, db
import os
import requests as req
from flask import render_template, request, redirect, url_for
from sqlalchemy import desc
from app.models import Movie
from app.forms import AddForm, EditForm

DATA_API = os.environ.get("DATA_API")
DB_IMG_URL = "https://image.tmdb.org/t/p/w500/"


def get_movie_matches(movie_name):
    movies_list = []
    datas = req.get(
        f"https://api.themoviedb.org/3/search/movie?query={movie_name}&api_key={DATA_API}"
    )
    for movie_data in datas.json().get("results"):
        if movie_data.get("original_language") == "en":
            movie_fetched = {
                "title": movie_data.get("original_title"),
                "release": movie_data.get("release_date"),
                "id": movie_data.get("id"),
            }
            movies_list.append(movie_fetched)
    print(movies_list)
    return movies_list


@app.route("/")
def home():
    movies = db.session.query(Movie).order_by(desc(Movie.ranking)).all()
    for i in range(len(movies)):
        movies[i].ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    movie = db.session.get(Movie, movie_id)

    if form.validate_on_submit():
        movie.review = form.review.data
        movie.rating = form.rating.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.session.get(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add_movie", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        all_movies_found = get_movie_matches(movie_title)
        return render_template("select.html", movies_found=all_movies_found)

    return render_template("add.html", form=form)


@app.route("/find", methods=["GET", "POST"])
def find_and_store():
    id = request.args.get("id")
    response = req.get(
        f"https://api.themoviedb.org/3/movie/{id}?api_key={DATA_API}"
    ).json()
    print(response)
    new_movie = Movie(
        title=response["original_title"],
        year=response["release_date"],
        description=response["overview"],
        img_url=f"{DB_IMG_URL}{response['poster_path']}",
    )
    print(
        "THIS IS THE PATH" + f"{DB_IMG_URL}{response['poster_path']}",
    )
    db.session.add(new_movie)
    db.session.commit()
    movie = Movie.query.filter_by(title=response["original_title"]).first()
    return redirect(url_for("edit", id=movie.id))
