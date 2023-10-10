import plotly.express
from matplotlib import pyplot as plt


style = {
    "figure.figsize": (8, 4),
    "axes.facecolor": (0.0, 0.0, 0.0, 0),
    "axes.edgecolor": "white",
    "axes.labelcolor": "white",
    "figure.facecolor": (1.0, 1.0, 1.0, 0),  # red   with alpha = 30%
    "savefig.facecolor": (0.0, 0.0, 0.0, 0),
    "patch.edgecolor": "#0e1117",
    "text.color": "white",
    "xtick.color": "blue",
    "ytick.color": "blue",
    "grid.color": "blue",
    "font.size": 12,
    "axes.labelsize": 18,
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
}


def load_pie(dataframe,n,v):
    import plotly.express as px
    figure_pie_chart = px.pie(dataframe,names=n,values=v)
    return figure_pie_chart

def load_pieTEST(dataframe,n,v):
    import plotly.express as px
    figure_pie_chart = px.pie(dataframe,
        names=n, values=v, color=dataframe[n],
            color_discrete_sequence=px.colors.carto.Earth_r)
    return figure_pie_chart


def load_graph2(dataframe):
    import plotly.express as px
    fig = px.scatter(
        dataframe,
        x="GDP",
        y="Life expectancy",
        size="Population",
        color="continent",
        hover_name="Country",
        log_x=True,
        size_max=60,
    )
    return fig

def plotlyBar(dataframe,x,y):
    import plotly.express as px
    fig = px.bar(dataframe, x=dataframe[x], y=dataframe[y],
        color=dataframe[x],color_discrete_sequence=px.colors.carto.Earth_r)
    return fig



