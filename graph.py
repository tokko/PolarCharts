#!/usr/bin/python3
import plotly.graph_objects as go
import itertools
import sys

# IMPORTANT NOTICE: This scrips was modified to run on a windows host. If you desire to run this on a mac or linux based system then you need to change the double backslashes in all file paths to a single forward slash.
def plot(x, y, graphName):
    fig = go.Figure(data=go.Barpolar(
        r = x, 
        theta = y,
        marker_color=["#C55" for _ in y],
        width=[5 for x in range(len(x))]
    ))
    # The disabled code underneath merely applies styling to the chart. It was disabled when plotly was upgraded with breaking changes. Feel free to play around with the new version.
    #fig.update_layout(template=None, 
    #        polar=dict(
    #            radialaxis = dict(range=[0,8.3],showticklabels=False)
    #           ),
    #       angularaxis=dict(
    #           range=[0,180],
    #           showticklabels=False)
    #         )
    #  fig.update_layout(
    #          showlegend = False,
    #          polar = dict(sector = [0,180])
    #          )
    # fig.update_polars(dict(angularaxis=dict(rotation=90, direction='clockwise'), sector=[0, 360]))
    fig.write_image("graphs\\%s.pdf"%graphName)
    fig.write_image("graphs\\%s.jpeg"%graphName)

def getData(path):
    f = open(path, mode='r')
    data = f.read()
    return data

def sanitize_data(data):
    return list(filter(lambda a: a != 0, [abs(x) for x in data]))

def plotDataFile(path, graphName):
    data = getData(path)
    fd = sanitize_data([int(float(a)) for a in filter(lambda a: a != "", data.split("\n"))])
    plot([1 for x in range(len(fd))], fd, graphName)

for fileName in sys.argv[1:]:
    name = fileName.split("\\")[1].split(".")[0]
    plotDataFile(fileName, name)
