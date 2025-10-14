
# This program highlights a user-specified country on a world map using Plotly.

# How it works:
# 1. The user is prompted to enter the name of a country.
# 2. A dataset is created with the country and a fixed value (e.g., 100).
# 3. A choropleth map is generated using Plotly Express.
# 4. If the entered country is valid (recognized by Plotly), the map is shown.
# 5. If the country is not valid, the user is asked to enter a new one.

# Validation is done by checking:
# - if `fig.data` exists (i.e. Plotly processed the data),
# - and if the country location is not `NaN`.

# This loop continues until a valid country name is provided.



import plotly.express as px
import pandas as pd

while True:
    country = input('Enter the name of the country: ')

    data = {
    'Country': [country],
    'Values': [100]}

    fig = px.choropleth(
        data,
        locations='Country',
        locationmode='country names',
        color='Values',
        color_continuous_scale='Inferno',
        title=f'Country highlighted {country}')
    if fig.data and not pd.isnull(fig.data[0]['locations']).all():
        fig.show()
        break
    else:
        print(f"'{country}' is not recognized. Please enter a valid country name.")
