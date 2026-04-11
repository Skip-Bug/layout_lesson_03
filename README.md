# Библиотека книг

Онлайн-каталог книг с возможностью читать их прямо в браузере.

## 📖 Читать книги онлайн

**[Открыть библиотеку](https://skip-bug.github.io/layout_lesson_03/)** — нажмите и читайте сразу, ничего не скачивая.

## 🖼️ Скриншот
<img width="1915" height="1313" alt="Screenshot 2026-04-11 183637" src="https://github.com/user-attachments/assets/435b62c5-15ea-46d8-896d-1b1019b2ab3a" />
---

## 👨‍💻 Для разработчиков

> Ниже — технические детали для тех, кто хочет запустить проект локально или доработать.

### Установка и запуск

Требуется Python 3.8+


```bash
git clone https://github.com/skip-bug/layout_lesson_03.git

cd layout_lesson_03

pip install -r requirements.txt

python render_website.py
```

Откройте `http://localhost:5500` в браузере.

### Структура проекта

```
layout_lesson_03/
├── render_website.py      # Скрипт генерации сайта
├── template.html          # Jinja2 шаблон
├── meta_data.json         # Данные о книгах
├── index.html             # Редирект на первую страницу
├── pages/                 # Сгенерированные страницы
├── media/                 # Обложки книг
└── static/                # CSS, JS файлы
```

### Формат данных (meta_data.json)

```json
[
  {
    "title": "Название книги",
    "author": "Автор",
    "genres": "Жанр1, Жанр2",
    "img_src": "media/cover.jpg",
    "book_path": "books/book.pdf"
  }
]
```

### Зависимости

```
jinja2==3.1.6
livereload==2.7.1
more-itertools==10.5.0
```

---

## 🎓 Цель проекта

Код написан в образовательных целях на курсе [dvmn.org](https://dvmn.org/) по веб-разработке.
