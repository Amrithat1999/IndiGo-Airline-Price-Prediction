from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
d=pd.read_csv('IndiGo_Data_Set.csv')
model = pickle.load(open("Airline_pickle.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("price_airline.html")

@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Departure Date
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)

        # Departure Time
        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)

        # Arrival Date
        date_arr = request.form["Arrival_Time"]
        Arrival_day = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").day)
        Arrival_month = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").month)

        #Arrival Time
        Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)

        # Total Stops
        Total_stops = int(request.form["stops"])

        # Source
        Source = request.form["Source"]
        if (Source == 'Banglore'):
            s_Banglore=1
            s_Chennai = 0
            s_Cochin=0
            s_Delhi = 0
            s_Hyderabad=0
            s_Kolkata = 0
            s_Mumbai = 0
            s_New_Delhi=0
            s_kannur=0

        elif (Source == 'Channai'):
            s_Banglore = 0
            s_Chennai = 1
            s_Cochin = 0
            s_Delhi = 0
            s_Hyderabad = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_New_Delhi = 0
            s_kannur = 0

        elif (Source == 'Cochin'):
            s_Banglore = 0
            s_Chennai = 0
            s_Cochin = 1
            s_Delhi = 0
            s_Hyderabad = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_New_Delhi = 0
            s_kannur = 0

        elif (Source == 'Delhi'):
            s_Banglore = 0
            s_Chennai = 0
            s_Cochin = 0
            s_Delhi = 1
            s_Hyderabad = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_New_Delhi = 0
            s_kannur = 0

        elif (Source == 'Hyderabad'):
            s_Banglore = 0
            s_Chennai = 0
            s_Cochin = 0
            s_Delhi = 0
            s_Hyderabad = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_New_Delhi = 0
            s_kannur = 0

        elif (Source == 'Kolkata'):
            s_Banglore = 0
            s_Chennai = 0
            s_Cochin = 0
            s_Delhi = 0
            s_Hyderabad = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_New_Delhi = 0
            s_kannur = 0

        elif (Source == 'Mumbai'):
            s_Banglore = 0
            s_Chennai = 0
            s_Cochin = 0
            s_Delhi = 0
            s_Hyderabad = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_New_Delhi = 0
            s_kannur = 0

        elif (Source == 'New Delh'):
            s_Banglore = 0
            s_Chennai = 0
            s_Cochin = 0
            s_Delhi = 0
            s_Hyderabad = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_New_Delhi = 1
            s_kannur = 0

        elif (Source == 'kannur'):
            s_Banglore = 0
            s_Chennai = 0
            s_Cochin = 0
            s_Delhi = 0
            s_Hyderabad = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_New_Delhi = 0
            s_kannur = 1

        else:
            s_Banglore = 0
            s_Chennai = 0
            s_Cochin = 0
            s_Delhi = 0
            s_Hyderabad = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_New_Delhi = 0
            s_kannur = 0

        # Destination
        Source = request.form["Destination"]
        if (Source == 'Chennai'):
            d_Banglore = 0
            d_Chennai = 1
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_kannur = 0
            d_Kolkata = 0
            d_Mumbai = 0
            d_New_Delhi = 0

        elif (Source == 'Banglore'):
            d_Banglore = 1
            d_Chennai = 0
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_kannur = 0
            d_Kolkata = 0
            d_Mumbai = 0
            d_New_Delhi = 0

        elif (Source == 'Cochin'):
            d_Banglore = 0
            d_Chennai = 0
            d_Cochin = 1
            d_Delhi = 0
            d_Hyderabad = 0
            d_kannur = 0
            d_Kolkata = 0
            d_Mumbai = 0
            d_New_Delhi = 0

        elif (Source == 'Delhi'):
            d_Banglore = 0
            d_Chennai = 0
            d_Cochin = 0
            d_Delhi = 1
            d_Hyderabad = 0
            d_kannur = 0
            d_Kolkata = 0
            d_Mumbai = 0
            d_New_Delhi = 0

        elif (Source == 'Hyderabad'):
            d_Banglore = 0
            d_Chennai = 0
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 1
            d_kannur = 0
            d_Kolkata = 0
            d_Mumbai = 0
            d_New_Delhi = 0

        elif (Source == 'kannur'):
            d_Banglore = 0
            d_Chennai = 0
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_kannur = 1
            d_Kolkata = 0
            d_Mumbai = 0
            d_New_Delhi = 0

        elif (Source == 'Kolkata'):
            d_Banglore = 0
            d_Chennai = 0
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_kannur = 0
            d_Kolkata = 1
            d_Mumbai = 0
            d_New_Delhi = 0

        elif (Source == 'Mumbai'):
            d_Banglore = 0
            d_Chennai = 0
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_kannur = 0
            d_Kolkata = 0
            d_Mumbai = 1
            d_New_Delhi = 0

        elif (Source == 'New Delh'):
            d_Banglore = 0
            d_Chennai = 0
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_kannur = 0
            d_Kolkata = 0
            d_Mumbai = 0
            d_New_Delhi = 1

        else:
            d_Banglore = 0
            d_Chennai = 0
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_kannur = 0
            d_Kolkata = 0
            d_Mumbai = 0
            d_New_Delhi = 0

        prediction = model.predict([[
            Total_stops,Journey_day,Journey_month,Dep_hour,Dep_min,
            Arrival_month,Arrival_day,Arrival_hour,Arrival_min,s_Banglore,
            s_Chennai,s_Cochin,s_Delhi,s_Hyderabad,s_Kolkata,s_Mumbai,s_New_Delhi,s_kannur,
            d_Banglore,d_Chennai,d_Cochin,d_Delhi,d_Hyderabad,d_kannur,d_Kolkata,d_Mumbai,d_New_Delhi,

        ]])

        output = round(prediction[0], 2)

        return render_template('price_airline.html', prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("price_airline.html")

if __name__ == "__main__":
    app.run(debug=True)
