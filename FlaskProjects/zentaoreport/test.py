import pygal
import data  # 数据库获取数据模块
from flask import Flask, render_template, request
# import datetime
# from flask.ext.bootstrap import Bootstrap

app = Flask(__name__, static_url_path='/static')


@app.route('/test/', methods=['GET', 'POST'])
def cc():
    pl = data.getpid()
    # pid = 49
    # l1,l2,l3 = data.getdata(pid) # '''l1 未解决按指派对象，l2 已解决按结局方案，l3 已解决按解决者'''

    titleList = ['未解决 - 严重程度', '未解决 - 开发人员',
                 '已解决 - 解决方案', '新增 - 严重程度', '新增 - 测试人员']
    chartList = []
    tabelList = []
    lineList = []
    X = 49
    P = pl[0]
    if request.method == 'POST':
        # print(request.form)
        # if request.form['select'] in [p['name'] for p in pl]:
        for p in pl:
            if request.form['select'] == p['name']:
                X = p['id']
                P = p
                # print(X)
        for item in data.getdata(X):
            # legend_at_bottom=True
            bar_chart = pygal.Bar(legend_at_bottom=True)
            for i in item:
                bar_chart.add(str(i['la']), i['num'], rounded_bars=4)
            tabelList.append(bar_chart.render_table(
                style=True, transpose=False))
            chartList.append(bar_chart.render_data_uri())
        # 曲线展示 legend_at_bottom=True
        for testlist in data.getdataline(X):
            line_chart = pygal.Line(legend_at_bottom=True, x_label_rotation=20)
            newlist = []
            LL = []
            for item in testlist:
                newlist.append([i for i in item.values()])
            severity = list(set([i['lb'] for i in testlist]))
            # print(severity)
            date = sorted(list(set([i['la'] for i in testlist])))
            # print(date)
            for s in severity:
                for d in date:
                    t = 0
                    for item in newlist:
                        if (item[1] == s) & (item[0] == d):
                            t = item[2]
                            break
                    LL.append(t)
            line_chart.x_labels = date
            i = 0
            j = len(date)
            for s in severity:
                line_chart.add('%s' % s, LL[i:j])
                del LL[i:j]
            lineList.append(line_chart.render_data_uri())

    else:
        # 列表展示 legend_at_bottom=True
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
            newlist = []
            LL = []
            for item in testlist:
                newlist.append([i for i in item.values()])
            severity = list(set([i['lb'] for i in testlist]))
            # print(severity)
            date = sorted(list(set([i['la'] for i in testlist])))
            # print(date)
            for s in severity:
                for d in date:
                    t = 0
                    for item in newlist:
                        if (item[1] == s) & (item[0] == d):
                            t = item[2]
                            break
                    LL.append(t)
            line_chart.x_labels = date
            i = 0
            j = len(date)
            for s in severity:
                line_chart.add('%s' % s, LL[i:j])
                del LL[i:j]
            # tabelList.append(line_chart.render_table(
            #     style=True, transpose=False))
            lineList.append(line_chart.render_data_uri())

    # return render_template('test.html', chart=chartList, title=titleList,
    # table=tabelList, line=lineList, pid=pl, x=X, p=P)
    return render_template('test.html', chart=chartList + lineList, title=titleList, table=tabelList, pid=pl, x=X, p=P)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
