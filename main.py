from bokeh.plotting import figure, show
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.models import ColumnDataSource
import pandas as pd

df = pd.read_csv('imdb_movie_metadata.csv', encoding="utf8")
df.dropna(inplace=True)  # Drop rows with missing attributes
df.drop_duplicates(inplace=True) # Remove duplicates
df.reset_index(drop=True ,inplace=True)  # Reset index
df.sort_index(axis=1, inplace=True)  #Sort by name

df_group = df['color'].value_counts()
print(df_group)

print(df)

Columns = [TableColumn(field=Ci, title=Ci) for Ci in df.columns]
source = ColumnDataSource(df)
data_table = DataTable(autosize_mode='fit_viewport', columns=Columns, source=source)

show(data_table)
