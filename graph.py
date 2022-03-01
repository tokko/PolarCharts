#!/usr/bin/python3
import plotly.graph_objects as go
import itertools

def plot(x, y, graphName):
    fig = go.Figure(data=go.Barpolar(
        r = x, 
        theta = y,
        width=[5 for x in range(len(x))]
    ),
    )
    fig.update_layout(template=None, 
            polar=dict(
                radialaxis = dict(
                    showticklabels=False
                    )
                ), 
            angularaxis=dict(
                range=[0,180],
                showticklabels=False)
            )
    fig.update_layout(
            showlegend = False,
            polar = dict(sector = [0,180]
                )
            )
   # fig.update_polars(dict(angularaxis=dict(rotation=90, direction='clockwise'), sector=[0, 360]))
    fig.write_image("%s.jpeg"%graphName)

def getData(path):
    f = open(path, mode='r')
    data = f.read()
    f.close
    return data

def plotDataFile(path, graphName):
    data = getData(path)
    fd = [int(float(a)) for a in filter(lambda a: a != "", data.split("\n"))]
    groups = itertools.groupby(fd, key=lambda a: a)
    m = [(a, len(list(b))) for a, b in groups]
    plot([1 for x in range(len(fd))], fd, graphName)

plotDataFile("data2/flow_kd_fiber.txt", "flow_kd_fiber")
plotDataFile("data2/flow_kd_nuclear.txt", "flow_kd_nuclear")
plotDataFile("data2/flow_wt_fiber.txt", "flow_wt_fiber")
plotDataFile("data2/flow_wt_nuclear.txt", "flow_wt_nuclear")
plotDataFile("data2/static_kd_fiber.txt", "static_kd_fiber")
plotDataFile("data2/static_kd_nuclear.txt", "static_kd_nuclear")
plotDataFile("data2/static_wt_fiber.txt", "static_wt_fiber")
plotDataFile("data2/static_wt_nuclear.txt", "static_wt_nuclear")
