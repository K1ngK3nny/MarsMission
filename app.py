from flask import Flask, render_template
import pymongo

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.marsmission     
collection = db.marsmission 



@app.route("/scrape")
def scrape():
    mars_facts = mongo.db.mars_facts
    mars_facts_data = mission_to_mars.scrape()
    mars_facts.update(
        {},
        mars_facts_data,
        upsert=True
        )


if __name__ == "__main__":
    app.run(debug=True)