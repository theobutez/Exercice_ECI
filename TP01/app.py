from flask import Flask, render_template
app = Flask(__name__)

# Données de films
pictures = [
    {"id": 0, "title": "Inception", "director": "Christopher Nolan"},
    {"id": 1, "title": "The Shawshank Redemption", "director": "Frank Darabont"},
    {"id": 2, "title": "Pulp Fiction", "director": "Quentin Tarantino"},
    {"id": 3, "title": "The Godfather", "director": "Francis Ford Coppola"},
    {"id": 4, "title": "The Dark Knight", "director": "Christopher Nolan"}
]

# Page d'accueil
@app.route('/')
def home():
    return render_template('home.html', pictures=pictures)

# Page de détails du film
@app.route('/picture/<int:id>')
def picture(id):
    picture = next((pic for pic in pictures if pic['id'] == id), None)
    if picture:
        return render_template('picture.html', picture=picture)
    return "Film non trouvé", 404

if __name__ == '__main__':
    app.run(debug=True)

