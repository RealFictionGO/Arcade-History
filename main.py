from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/library')
def library():
  return render_template("library.html")

@app.route('/library/snake')
def snake():
  return render_template("snake_site.html")

@app.route('/library/snake/game')
def play_snake():
  return render_template("")

@app.route('/library/pac-man')
def pac_man():
  return render_template("pac_man_site.html")

@app.route('/library/pac-man/game')
def play_pac_man():
  return render_template("")

@app.route('/library/tetris/game')
def play_tetris():
  return render_template("")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)