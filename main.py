from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/library')
def library():
  return render_template("library.html")

@app.route('/library/pacman')
def pac_man():
  return render_template("pacman.html")

@app.route('/library/snake')
def snake_page():
  return render_template("snakestron.html")

@app.route('/library/snake/game')
def snake():
  return render_template("snake.html")

@app.route('/library/tetris')
def tetris_page():
  return render_template("tetrisstrona.html")

@app.route('/library/tetris/game')
def tetris():
  return render_template("tetris.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)