from flask import Flask, render_template, redirect, url_for
app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
  return render_template("glowna.html")

@app.route('/admin')
def admin():
  return redirect('https://youtu.be/dQw4w9WgXcQ')

@app.route('/sources')
def sources():
  return render_template("zrodlawykorzystane.html")

@app.route('/libraryofgames')
def library():
  return render_template("bibliotekagier.html")

@app.route('/libraryofgames/pacman')
def pac_man_site():
  return render_template("pacmanstrona.html")

@app.route('/libraryofgames/pacman/game')
def pac_man():
  return render_template("pacman.html")

@app.route('/libraryofgames/snake')
def snake_page():
  return render_template("snakestrona.html")

@app.route('/libraryofgames/snake/game')
def snake():
  return render_template("snake.html")

@app.route('/libraryofgames/tetris')
def tetris_page():
  return render_template("tetrisstrona.html")

@app.route('/libraryofgames/tetris/game')
def tetris():
  return render_template("tetris.html")

if __name__ == '__main__':
  app.run(port=8080, debug=True)