# coding:utf-8

import codecs


# 数据存储器
class DataOutput(object):
    def __init__(self):
        self.datas = []

    # 解析的数据存储到内存中
    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 将存储的数据输出为指定的文件格式，此处我们为HTML格式
    def output_html(self):
        fout = codecs.open('baike.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('<tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
