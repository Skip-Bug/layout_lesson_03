"""Рендер страниц сайта для библиотеки."""
import argparse
import json
import math
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def create_parser():
    """Добавляет аргументы для скрипта."""
    parser = argparse.ArgumentParser(
        description='Книжная библиотека'
    )
    parser.add_argument(
        '-db', '--data_base',
        default='meta_data.json',
        help='База библиотеки (meta_data.json по умолчанию)'
    )
    return parser


def load_books():
    """Загружает книги из базы данных и возвращает отсортированный список."""
    parser = create_parser()
    args = parser.parse_args()
    if not os.path.exists(args.data_base):
        print(f'Файл {args.data_base} не найден')
        return
    with open(args.data_base, 'r', encoding='utf-8') as file:
        data_books = json.load(file)
    return sorted(data_books, key=lambda book: book['title'])


def get_pages():
    """Формирует список страниц для отображения книг с пагинацией."""
    books = load_books()
    for book in books:
        book['genres_list'] = [
            genre.strip()
            for genre in book['genres'].replace('.', ',').split(',')
            if genre.strip()
        ]

    books_on_pages = 10
    chunks = list(chunked(books, books_on_pages))
    total_pages = math.ceil(len(books) / books_on_pages)

    pages = []
    for page_num, book_group in enumerate(chunks, start=1):
        prev_page = f"index{page_num-1}.html" if page_num > 1 else None
        next_page = (
            f"index{page_num+1}.html" if page_num < total_pages else None
        )
        pages.append({
            'books': book_group,
            'current_page': page_num,
            'total_pages': total_pages,
            'prev_link': prev_page,
            'next_link': next_page
        })
    return pages


def on_reload(path=None):
    """Рендерит страницы сайта для библиотеки."""
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    pages = get_pages()
    for page in pages:
        books_rows = list(chunked(page['books'], 2))
        filename = os.path.join('pages', f"index{page['current_page']}.html")
        rendered_page = template.render(
            books_rows=books_rows,
            current_page=page['current_page'],
            total_pages=page['total_pages'],
            prev_link=page['prev_link'],
            next_link=page['next_link']
        )
        with open(filename, 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    os.makedirs('pages', exist_ok=True)
    on_reload()
    redirect_html = (
        '<!DOCTYPE html>'
        '<html><head>'
        '<meta http-equiv="refresh" content="0; url=pages/index1.html">'
        '</head><body></body></html>'
    )
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(redirect_html)

    server = Server()

    server.watch('template.html', on_reload)
    server.watch(args.data_base, on_reload)
    server.serve(root='.')
