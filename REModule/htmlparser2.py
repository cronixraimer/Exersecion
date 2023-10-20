from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
        else:
            print('>>> Single-line Comment')
            print(data)

    def handle_data(self, data):
        if '\n' != data:
            print('>>> Data')
            print(data)

html_code = ''
x = int(input())
for i in range(x):
    html_code += input().rstrip()
    html_code += '\n'

parser = MyHTMLParser()
parser.feed(html_code)
parser.close()
