import streamlit as st
import pandas as pd
from datetime import datetime

# Read the ecommerce data into a Pandas DataFrame
data = pd.read_csv('ecommerce.csv')

# Convert the 'date' column to datetime with the correct format
data['date'] = pd.to_datetime(data['date'], format='%d-%m-%Y')  # Updated format to '%d-%m-%Y'

# Declare a text input widget for the user to enter a date in dd/mm/yyyy format
st.title("Predictive Analysis for Ecommerce Data")
st.write("Enter date from 01-08-2023 to 10-08-2023")
user_date = st.text_input("Enter a date (dd-mm-yyyy): ")  # Updated format in the input label

# Convert the user-entered date to a Pandas datetime
try:
    user_date = datetime.strptime(user_date, "%d-%m-%Y")  # Updated format to '%d-%m-%Y'
    
    # Filter the data for the selected date
    selected_data = data[data['date'] == user_date]

    # Check if there is any data for the selected date
    if selected_data.empty:
        st.write("No data available for the provided date.")
    else:
        # Get information for the selected date
        purchases_on_date = selected_data['purchase'].values[0]
        items_sold_on_date = selected_data['items_sold'].values[0]

        avg_purchases_per_day = data['purchase'].mean()

        if purchases_on_date > avg_purchases_per_day:
            more_purchases_than_avg = "more" 
        else:
            more_purchases_than_avg = "not more" 

        # Display the information to the user
        st.write("purchases: ", purchases_on_date)
        st.write("Items sold: ", items_sold_on_date)
        st.write("Purchases were " + more_purchases_than_avg +" than average.")
except ValueError:
    st.write("Please enter a valid date in dd-mm-yyyy format.")  # Updated format in the error message
