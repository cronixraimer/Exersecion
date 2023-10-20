from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, att):
        print(tag)
        for i in att:
            print(f'-> {i[0]} > {i[1]}')


html_code = ''
x = int(input())
for i in range(x):
    html_code += input().rstrip()
    html_code += '\n'

parser = MyHTMLParser()
parser.feed(html_code)
parser.close()
