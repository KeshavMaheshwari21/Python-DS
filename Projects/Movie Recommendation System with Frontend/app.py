from flask import Flask, request, render_template
import pickle
import requests
import pandas as pd
from patsy import dmatrices

movies = pickle.load(open('models/movies_list.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))

app = Flask(__name__)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['original_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:5]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].original_title	)
    return recommended_movies_name, recommended_movies_poster

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/recommendation' , methods = ['GET','POST'])
def recommendation():
    movie_list = movies['original_title'].values
    status = False
    if request.method == 'POST':
        try:
            if request.form:
                movies_name = request.form['movies']
                recommended_movies_name, recommended_movies_poster = recommend(movies_name)
                status = True

                return render_template("prediction.html", movies_name = recommended_movies_name, poster = recommended_movies_poster, movie_list = movie_list, status = status)


        except Exception as e:
            error = {'error': e}
            return render_template("prediction.html",error = error, movie_list = movie_list, status = status)

    else:
        return render_template("prediction.html", movie_list = movie_list, status = status)



if __name__ == '__main__':
    app.debug = True
    app.run()