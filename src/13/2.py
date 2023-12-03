import numpy as np
import plotly.express as px
import seaborn as sns

# 1
penguins_data = sns.load_dataset("penguins")

penguins_data.info()

first_rows = penguins_data.head(5)
print(first_rows)

assert (
    str(first_rows)
    == "  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \\\n0  Adelie  Torgersen            39.1           18.7              181.0   \n1  Adelie  Torgersen            39.5           17.4              186.0   \n2  Adelie  Torgersen            40.3           18.0              195.0   \n3  Adelie  Torgersen             NaN            NaN                NaN   \n4  Adelie  Torgersen            36.7           19.3              193.0   \n\n   body_mass_g     sex  \n0       3750.0    Male  \n1       3800.0  Female  \n2       3250.0  Female  \n3          NaN     NaN  \n4       3450.0  Female  "
)


# 2
l = px.line(
    data_frame=penguins_data,
    x="bill_length_mm",
    y="body_mass_g",
    symbol="sex",
    width=600,
)

l

assert l.data[0]["mode"] == "markers+lines"

s = px.scatter(
    data_frame=penguins_data,
    x="bill_length_mm",
    y="body_mass_g",
    color="species",
    symbol="sex",
    width=600,
)

s

assert s.data[0]["mode"] == "markers"

l_s = sns.lineplot(
    data=penguins_data, x="bill_length_mm", y="body_mass_g", hue="species", style="sex"
)

l_s

assert np.array_equal(
    l_s.properties()["xticks"],
    np.array([30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0]),
)

# 3
b = px.bar(
    data_frame=penguins_data,
    y="island",
    facet_row="species",
    pattern_shape="species",
    color="species",
    facet_row_spacing=0.10,
    width=600,
    height=600,
)

b

assert b.data[0].orientation == "h"
