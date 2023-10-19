from html.parser import HTMLParser

def print_attrs(attributes):
    for i in attributes:
        print(f'-> {i[0]} > {i[1]}')


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        print_attrs(attrs)

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        print_attrs(attrs)


html_code = ''.join(input() for i in range(int(input())))

parser = MyHTMLParser()
parser.feed(html_code)
