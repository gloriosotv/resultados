from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_games():
    conn = sqlite3.connect('data/data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM games')
    games = cursor.fetchall()
    conn.close()
    return games

@app.route('/')
def index():
    games = get_games()
    return render_template('index.html', games=games)

if __name__ == '__main__':
    app.run(debug=True)

