class HtmlOutputer(object):
    def __init__(self):
        self.dataList = []

    def collect_data(self, data):
        if data is None:
            return
        self.dataList.append(data)


    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.dataList:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])

            #string.replace(u'\xa0', u' ')
            fout.write("<td>%s</td>" % data['summary']) # data['summary'].encode('utf-8')
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")