from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	best = ['Yoav',"Uri","Amit"]
	worst = ["meetX"]
	opposite_day = True
	return render_template("index.html",best = best,worst = worst,opposite_day=opposite_day)

if __name__ == '__main__':
   app.run(debug = True)
