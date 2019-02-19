from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if not data == '\n':
            print(">>> Data")
            print(data)

    def handle_comment(self, data):
        if '\n' not in data:
            print(">>> Single-line Comment")
            print(data)
        else:
            print(">>> Multi-line Comment")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()