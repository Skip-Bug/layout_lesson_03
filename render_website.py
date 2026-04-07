import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler

with open('meta_data.json', 'r', encoding='utf-8') as file:
    meta_data = file.read()
data_books = json.loads(meta_data)

books = sorted(data_books, key=lambda book: book['title'])
# print(books)
# for book in books:
#     print(book['title'])
#     print(book['author'])
#     print(book['genres'])
#     print(book['comments'])


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(books=books)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()