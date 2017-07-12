from flask import Flask
from flask import jsonify
app = Flask(__name__)

myArr = ["Atlanta Braves", 
"Florida Marlins", 
"New York Mets", 
"Philadelphia Phillies", 
"Washington Nationals",  
"Chicago Cubs", 
"Cincinnati Reds", 
"Houston Astros", 
"Milwaukee Brewers", 
"Pittsburgh Pirates", 
"St. Louis Cardinals", 
"Arizona Diamondbacks", 
"Colorado Rockies", 
"Los Angeles Dodgers", 
"San Diego Padres", 
"San Francisco Giants",  
"Baltimore Orioles", 
"Boston Red Sox", 
"New York Yankees", 
"Tampa Bay Rays", 
"Toronto Blue Jays", 
"Chicago White Sox", 
"Cleveland Indians", 
"Detroit Tigers", 
"Kansas City Royals", 
"Minnesota Twins",  
"Los Angeles Angels", 
"Oakland Athletics", 
"Seattle Mariners", 
"Texas Rangers"]

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/json")
def json():
    return jsonify(myArr) 

if __name__ == "__main__":
    app.run()