import pygal
import data  # 数据库获取数据模块
from flask import Flask, render_template, request
import datetime

app = Flask(__name__, static_url_path='/static')


@app.route('/test/', methods=['GET', 'POST'])
def cc():
    pl = data.getpid()
    titleList = ['未解决 - 严重程度', '未解决 - 开发人员',
                 '已解决 - 解决方案', '新增 - 严重程度', '新增 - 测试人员']
    chartList = []
    tabelList = []
    lineList = []
    X = 49
    P = pl[0]
    if request.method == 'POST':
        for p in pl:
            if request.form['select'] == p['name']:
                X = p['id']
                P = p
    # 柱状图展示
    for item in data.getdata(X):
        bar_chart = pygal.Bar(legend_at_bottom=True)
        for i in item:
            bar_chart.add(str(i['la']), i['num'], rounded_bars=4)
        tabelList.append(bar_chart.render_table(
            style=True, transpose=False))
        chartList.append(bar_chart.render_data_uri())
    # 曲线展示
    for testlist in data.getdataline(X):
        line_chart = pygal.Line(legend_at_bottom=True)
        date, severity, num = data.formatdata(testlist)
        line_chart.x_labels = date
        for index, s in enumerate(severity):
            line_chart.add('%s' % s, num[index])
        lineList.append(line_chart.render_data_uri())

    return render_template('test.html', chart=chartList + lineList, title=titleList, table=tabelList, pid=pl, x=X, p=P)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
