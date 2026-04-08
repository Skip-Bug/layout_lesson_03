import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server


def load_books():
    with open('meta_data.json', 'r', encoding='utf-8') as file:
        data_books = json.load(file)
    return sorted(data_books, key=lambda book: book['title'])


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


def rebuild(path=None):
    books = load_books()
    rendered_page = template.render(books=books)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == '__main__':
    rebuild()

    server = Server()

    server.watch('template.html', rebuild)
    server.watch('meta_data.json', rebuild)
    server.serve(root='.')
