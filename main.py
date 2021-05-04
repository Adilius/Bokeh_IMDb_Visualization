from bokeh.plotting import figure, show
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.models import ColumnDataSource
import pandas as pd

print("Hello world")

csv_dataframe = pd.read_csv('imdb_movie_metadata.csv', encoding="utf8")
csv_dataframe.dropna(inplace=True)  # Drop rows with missing attributes
csv_dataframe.drop_duplicates(inplace=True) # Remove duplicates
csv_dataframe.reset_index(drop=True ,inplace=True)  # Reset index

print(csv_dataframe)

Columns = [TableColumn(field=Ci, title=Ci) for Ci in csv_dataframe.columns]
data_table = DataTable(autosize_mode='fit_viewport', columns=Columns, source=ColumnDataSource(csv_dataframe))

show(data_table)
