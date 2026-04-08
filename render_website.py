import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
import os


def load_books():
    with open('meta_data.json', 'r', encoding='utf-8') as file:
        data_books = json.load(file)
    return sorted(data_books, key=lambda book: book['title'])


def on_reload(path=None):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    books = load_books()
    rendered_page = template.render(books=books)
    with open('index.html', 'w', encoding="utf8") as f:
        f.write(rendered_page)
    print(f"Site rebuilt at {os.path.getmtime('index.html')}")

    print("Site rebuilt")


if __name__ == '__main__':
    on_reload()

    server = Server()

    server.watch('template.html', on_reload)
    server.watch('meta_data.json', on_reload)
    server.serve(root='.')
