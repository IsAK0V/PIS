# Лабораторная работа №8

## Что сделано по заданию
- [x] Подключение jQuery **перед** остальными скриптами в `archive.html`
- [x] Файл `highlight-post.js` создан и подключён четвёртым
- [x] В шаблоне каждому `.one-post` добавлен `<div class="one-post-shadow"></div>`
- [x] CSS для `.one-post-shadow`: position:absolute, top/left:0, 100%×100%, background:black, z-index:-1, **opacity:0**
- [x] JS `$(document).ready(...)` — защита от выполнения до загрузки DOM
- [x] `.one-post` hover: `animate({opacity:'0.1'}, 300)` при наведении, `0` при уходе
- [x] **Задание**: `.header img` hover — ширина +20px, высота пропорционально, анимация 300 мс

## БД заполнена (27.02.2026)
Пользователи: admin/admin123, vasya/vasya123, anya/anya123, georgiy/geo123
Статьи: 4 записи


## Запуск
```bash
cd lab8/blog
python manage.py runserver   # БД уже заполнена
# http://127.0.0.1:8000/
# Навести на пост -> тёмная подсветка (0% -> 10% opacity за 300мс)
# Навести на логотип -> ширина +20px, высота пропорционально
```
