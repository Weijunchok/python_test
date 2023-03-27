# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd
# 
# # Load data from a JSON string
# data_str = '{"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]}'
# df = pd.read_json(data_str)
# 
# # Initialize the Dash app
# app = dash.Dash(__name__)
# 
# # Define the layout of the app
# app.layout = html.Div([
#     dcc.Graph(
#         id='my-chart',
#         figure={
#             'data': [
#                 {'x': df['x'], 'y': df['y'], 'type': 'line'}
#             ],
#             'layout': {
#                 'title': 'My Data'
#             }
#         }
#     )
# ])
# 
# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=False)
# import sqlalchemy
# import pandas as pd
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# 
# # Define the database connection parameters
# engine = sqlalchemy.create_engine('mysql+mysqlconnector://user:password@host/databsase')
# 
# # Load data from the database into a Pandas DataFrame
# df = pd.read_sql('SELECT * FROM humiture', engine)
# print(df)
# # Initialize the Dash app and define its layout
# app = dash.Dash(__name__)
# 
# app.layout = html.Div([
#     dcc.Graph(
#         id='my-chart',
#         figure={
#             'data': [
#                 {'x': df['Uploadtime'], 'y': df['Temp'], 'type': 'line'}
#             ],
#             'layout': {
#                 'title': 'Humiture'
#             }
#         }
#     )
# ])
# 
# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=False)

# import sqlalchemy
# import pandas as pd
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# 
# # Define the database connection parameters
# engine = sqlalchemy.create_engine('mysql+mysqlconnector://user:password@host/databsase')
# 
# # Load data from the database into a Pandas DataFrame
# df = pd.read_sql('SELECT * FROM humiture', engine)
# print(df)
# # Initialize the Dash app and define its layout
# app = dash.Dash(__name__)
# 
# app.layout = html.Div([
#     dcc.Graph(
#         id='my-chart',
#         figure={
#             'data': [
#                 {'x': df['Uploadtime'], 'y': df['Temp'], 'type': 'line'},
#                 {'x': df['Uploadtime'], 'y': df['Humi'], 'type': 'line'}
#             ],
#             'layout': {
#                 'title': 'Humiture'
#             }
#         }
#     )
# ])
# 
# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=False)

import sqlalchemy
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_table import DataTable
# Define the database connection parameters
engine = sqlalchemy.create_engine('mysql+mysqlconnector://user:password@host/databsase')

# Load data from the database into a Pandas DataFrame
df = pd.read_sql('SELECT * FROM humiture', engine)
total_data_points = df['Humi'].count()
# print(df['Humi'].count())
# Initialize the Dash app and define its layout
app = dash.Dash(__name__)
columns = [{'name': col, 'id': col} for col in df.columns]
print(columns)
app.layout = html.Div([
    html.H1(f'Total number of data points: {total_data_points}'),
    DataTable(
        id='data-table',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records')
    ),
    dcc.Graph(
        id='my-chart',
        figure={
            'data': [
                {'x': df['Uploadtime'], 'y': df['Temp'], 'type': 'line'},
                {'x': df['Uploadtime'], 'y': df['Humi'], 'type': 'line'}
            ],
            'layout': {
                'title': 'Humiture'
            }
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
