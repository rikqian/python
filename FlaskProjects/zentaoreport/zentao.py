import pygal      
import data #数据库获取数据模块
from flask import render_template,Flask
# from flask.ext.bootstrap import Bootstrap  

app = Flask(__name__,static_url_path='/static')


@app.route('/charts/')
def cc():
	l1,l2,l3 = data.getdata() # '''l1 未解决按指派对象，l2 已解决按结局方案，l3 已解决按解决者'''
	titleList = ['未解决按人员','已解决按方案','已解决待验证']
	chartList = []
	tabelList = []
	for item in [l1,l2,l3]:
		bar_chart = pygal.Bar(legend_at_bottom=True) 
		for i in item:
			bar_chart.add(str(i['la']),i['num'],rounded_bars = 4)
		tabelList.append(bar_chart.render_table(style=True, transpose=False))
		chartList.append(bar_chart.render_data_uri())

	# bar_chart1 = pygal.Bar()
	# for b in l1:
	# 	bar_chart1.add(str(b['la']),b['num'])
	# table1 = bar_chart1.render_table(style=True, transpose=False)
	# table1 = 'ba'
	return render_template( 'c1.html', chart = chartList,title = titleList,table = tabelList)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')