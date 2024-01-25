# TopMovies
TopMovies is a website that use CRUD to create your own top of movies. It use an API to get the data of the movie and make the list.

- Getting your api:
  Register and get the API KEY from themoviedb from their webpages -> https://developer.themoviedb.org/reference/intro/getting-started

- Configuration:
  - Install python-dotenv in your virtual environment and create a ".flaskenv" file in the main folder.
  - In .flaskenv create the next variables:
      FLASK_APP = topmovies.py
      SECRET_KEY = "your secret key"
      SQLALCHEMY_DATABASE_URI= "sqlite:///movies.db"
      DATA_API = "Your themoviedb api"
      FLASK_DEBUG=1 (optional)
  - Install the dependencies from requiriments.txt
  - That's all, now you can run the app.

