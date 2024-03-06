from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from plotly.graph_objs import scatter
import plotly.graph_objects as go



df = pd.read_csv('HREmployeeAttrition.csv')

app = Dash(__name__)
app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    #dcc.Graph(figure=px.histogram(df, x='MonthlyIncome', y='YearsAtCompany')),
    dcc.Graph(figure=px.scatter(df,x="MonthlyIncome", y="JobRole",color="Gender",size='MonthlyIncome',symbol="Gender")),
    dcc.Graph(figure=px.scatter(df,x="Age", y="MonthlyIncome",color="Gender",facet_col="Gender")),
    dcc.Graph(figure=px.icicle(df,path=[px.Constant("all"),"Gender","EducationField","Department"],color="Gender")),
    dcc.Graph(figure=px.parallel_categories(df,dimensions=['Gender', 'MaritalStatus', 'JobSatisfaction'],color="JobSatisfaction", color_continuous_scale=px.colors.sequential.Inferno,)),
    dcc.Graph(figure=px.violin(df,y="DistanceFromHome",color="OverTime",violinmode='overlay',)),
    dcc.Graph(figure=px.density_heatmap(df,x="JobLevel",y="YearsAtCompany",)),

])

# @callback(
#     Output('graph-content', 'figure'),
# )
# def update_graph(value):
#     dff = df[df.Department==value]
#     return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)