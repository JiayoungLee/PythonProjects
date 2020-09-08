# !/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Jayoung"

'''
gzbd graph
'''

import plotly, gzbd.gzbd_storage;


def draw_line_graph():
    result = gzbd.gzbd_storage.get_gzbd_data();
    x = [];
    y_diagnosis = [];
    y_cure = [];
    y_death = [];
    for item in result:
        x.append(item[2]);
        y_diagnosis.append(item[3]);
        y_cure.append(item[5]);
        y_death.append(item[6]);
    # 准备图轨数据
    # trace_1 = plotly.graph_objs.Scatter(
    #   x=[1, 2, 3, 4],
    #   y=[32, 44, 11, 66],
    #   name="散点图",
    #   mode='markers'
    # );

    trace_1 = plotly.graph_objs.Scatter(
        x=x,
        y=y_diagnosis,
        name="确诊数",
    );

    trace_2 = plotly.graph_objs.Scatter(
        x=x,
        y=y_cure,
        name="治愈数",
        # mode='markers' 默认折线图
    );

    trace_3 = plotly.graph_objs.Scatter(
        x=x,
        y=y_death,
        name="死亡数",
        # mode='markers' 默认折线图
    );
    line_data = [trace_1, trace_2, trace_3];

    # 设置画布布局
    layout = plotly.graph_objs.Layout(
        title="gzbd折线图",
        xaxis={"title": "时间"},
        yaxis={"title": "人数"}
    );

    # 融合 图轨数据 和 布局
    figure = plotly.graph_objs.Figure(data=line_data, layout=layout);

    # 输出
    plotly.offline.plot(figure, filename="/temp/line_graph.html", image="png");


def draw_bar_graph():
    # 准备图轨数据
    trace_1 = plotly.graph_objs.Bar(
        x=[1, 2, 3, 4],
        y=[32, 44, 11, 66],
        name="第一产业",
    );

    trace_2 = plotly.graph_objs.Bar(
        x=[1, 2, 3, 4],
        y=[13, 45, 21, 74],
        name="第二产业",
    );
    trace_3 = plotly.graph_objs.Bar(
        x=[1, 2, 3, 4],
        y=[54, 34, 26, 17],
        name="第三产业",
    );
    bar_data = [trace_1, trace_2, trace_3];

    # 设置画布布局
    layout = plotly.graph_objs.Layout(
        title="柱状图测试",
        xaxis={"title": "季度"},
        yaxis={"title": "产值"}
    );

    # 融合 图轨数据 和 布局
    figure = plotly.graph_objs.Figure(data=bar_data, layout=layout);

    # 输出
    plotly.offline.plot(figure, filename="/temp/bar_graph.html", image="png");


#
def draw_pie_graph():
    # 准备图轨数据
    trace_1 = plotly.graph_objs.Pie(
        labels=["产品一", "产品二", "产品三", "产品四", "产品五"],
        values=[13.4, 24.6, 33.2, 35.6, 56.1],
    );

    bar_data = [trace_1];

    # 设置画布布局
    layout = plotly.graph_objs.Layout(
        title="饼状图测试",

    );

    # 融合 图轨数据 和 布局
    figure = plotly.graph_objs.Figure(data=bar_data, layout=layout);

    # 输出
    plotly.offline.plot(figure, filename="/temp/pie_graph.html", image="png");


if __name__ == "__main__":
    draw_line_graph();
    # draw_bar_graph();
    # draw_pie_graph();
