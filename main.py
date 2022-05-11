from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/library')
def library():
  return render_template("library.html")

@app.route('/pacman')
def pac_man():
  return render_template("pacman.html")

@app.route('/snake')
def snake():
  return render_template("snake.html")

@app.route('/tetris')
def tetris():
  return render_template("tetris.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)