from flask import Flask, render_template,jsonify,request
import pandas as pd
import sqlite3
import plotly.express as px
import plotly
import json
import plotly.graph_objects as go
import logging

app = Flask(__name__)

logging.basicConfig(filename='application.log', level=logging.INFO)
app.logger.info("Flask app has started")

logging.basicConfig(filename='/home/hamsini.sankaran/w209/application.log', level=logging.INFO)

yr_filtered = pd.read_csv('/home/hamsini.sankaran/w209/static/yr_filtered.csv')
app.logger.info("read csv file:\n{}".format(yr_filtered.head()))


@app.route("/api")
def api():
    response = {"x": 5}
    return jsonify(response)

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/courses")
def trends():
    return render_template("courses.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/courses")
def courses():
    # Your logic here, for example:
    return render_template("courses.html")

@app.route("/trainers")
def trainers():
    # Your logic here, for example:
    return render_template("trainers.html")

@app.route("/events")
def events():
    # Your logic here, for example:
    return render_template("events.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/pricing")
def pricing():
    # Your logic here, for example:
    return render_template("pricing.html")


@app.route("/players/count")
def players_count():
    # Connect to the SQLite database
    conn = sqlite3.connect('/home/hamsini.sankaran/w209/players_20.db')
    cursor = conn.cursor()
    
    # Execute the query to get the count of rows in the Users table
    cursor.execute("SELECT COUNT(*) FROM Users")
    count = cursor.fetchone()[0]
    
    # Close the connection
    conn.close()
    
    return jsonify({"count": count})

@app.route("/players/get_nationality")
def get_nationality():
    player_name = request.args.get('player')
    
    if not player_name:
        return jsonify({"error": "player name is required!"}), 400 

    # Connect to the SQLite database
    conn = sqlite3.connect('/home/hamsini.sankaran/w209/players_20.db')
    cursor = conn.cursor()

    # Use parameterized query to prevent SQL injection
    cursor.execute("SELECT nationality FROM Users WHERE short_name=?", (player_name,))
    result = cursor.fetchone()

    #Close the connection
    conn.close()

    if result:
        return jsonify({"nationality": result[0]})
    else:
        return jsonify({"error": "Player not found!"}), 404

def plotly_sunburst_chart(data, year=2015):
    year_data = data[data['year'] == year]
    fig = px.sunburst(year_data, path=['region', 'state'], title='Regions and States')
    fig.update_traces(textfont=dict(size=25), insidetextfont=dict(size=16))
    fig.update_layout(margin=dict(t=40, l=0, r=0, b=0), height=600, width=1300)
    return fig

def updated_sunburst_chart(data):
    # Filter data for the year 2015
    yr_2015 = data[data['year'] == 2015]

    # Create the sunburst chart for 4th-grade math for the year 2015
    fig_math_4_2015 = go.Figure(px.sunburst(yr_2015,
                                          path=['region', 'state', 'avg_math_4_score', 'math_category_grade4'],
                                          values='avg_math_4_score'))

    # Update layout for the 4th-grade math chart
    fig_math_4_2015.update_layout(
        title="Interactive Exploration of Grade 4 Average Math in U.S. Regions (2015)",
        height=500,
        width=700,
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(l=30, r=30, t=30, b=30)
    )

    # Create the sunburst chart for 4th-grade reading for the year 2015
    fig_reading_4_2015 = go.Figure(px.sunburst(yr_2015,
                                             path=['region', 'state', 'avg_reading_4_score', 'reading_category_grade4'],
                                             values='avg_reading_4_score'))

    # Update layout for the 4th-grade reading chart
    fig_reading_4_2015.update_layout(
        title="Interactive Exploration of Grade 4 Average Reading in U.S. Regions (2015)",
        height=500,
        width=700,
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(l=30, r=30, t=30, b=30)
    )

    # Create the sunburst chart for 8th-grade math for the year 2015
    fig_math_8_2015 = go.Figure(px.sunburst(yr_2015,
                                          path=['region', 'state', 'avg_math_8_score', 'math_category_grade8'],
                                          values='avg_math_8_score'))

    # Update layout for the 8th-grade math chart
    fig_math_8_2015.update_layout(
        title="Interactive Exploration of Grade 8 Average Math in U.S. Regions (2015)",
        height=500,
        width=700,
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(l=30, r=30, t=30, b=30)
    )

    # Create the sunburst chart for 8th-grade reading for the year 2015
    fig_reading_8_2015 = go.Figure(px.sunburst(yr_2015,
                                             path=['region', 'state', 'avg_reading_8_score', 'reading_category_grade8'],
                                             values='avg_reading_8_score'))

    # Update layout for the 8th-grade reading chart
    fig_reading_8_2015.update_layout(
        title="Interactive Exploration of Grade 8 Average Reading in U.S. Regions (2015)",
        height=500,
        width=700,
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(l=30, r=30, t=30, b=30)
    )

    return fig_math_4_2015, fig_reading_4_2015, fig_math_8_2015, fig_reading_8_2015

@app.route("/")
def sunburst_chart():
    #fig_math_4_2015, fig_reading_4_2015, fig_math_8_2015, fig_reading_8_2015 = updated_sunburst_chart(yr_filtered)
    
    # Serialize the figures to JSON separately for both 4th-grade and 8th-grade
    #plot_json_math_4 = json.dumps(fig_math_4_2015, cls=plotly.utils.PlotlyJSONEncoder)
    #plot_json_reading_4 = json.dumps(fig_reading_4_2015, cls=plotly.utils.PlotlyJSONEncoder)
    
    #plot_json_math_8 = json.dumps(fig_math_8_2015, cls=plotly.utils.PlotlyJSONEncoder)
    #plot_json_reading_8 = json.dumps(fig_reading_8_2015, cls=plotly.utils.PlotlyJSONEncoder)
    
    #print('Sunburst Chart JSON (Math - 4th Grade):', plot_json_math_4)
    #print('Sunburst Chart JSON (Reading - 4th Grade):', plot_json_reading_4)
    #print('Sunburst Chart JSON (Math - 8th Grade):', plot_json_math_8)
    #print('Sunburst Chart JSON (Reading - 8th Grade):', plot_json_reading_8)

    return render_template("index.html")
                      #     plot_json_math_4=plot_json_math_4,
                      #     plot_json_reading_4=plot_json_reading_4,
                      #     plot_json_math_8=plot_json_math_8,
                      #     plot_json_reading_8=plot_json_reading_8)

@app.route("/sunburst")
def some_charts():
    #file="schools.jpeg"
    return render_template("w209.html")


@app.route("/temp")
def scrolly_tell():
    return render_template("index_scrolly.html")

if __name__ == "__main__":
    app.run()
    app.logger.setLevel(logging.INFO)
