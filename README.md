# md2coreui

Библиотека для преобразования Markdown в HTML со стилями компонентов CoreUI.

## Установка

```bash
pip install .
```

или для разработки:

```bash
pip install -e .
```

## Быстрый пример

```python
from md2coreui import convert

markdown = "# Заголовок\n\nЭто параграф с [ссылкой](https://example.com)."

html = convert(markdown)
print(html)
```

## Функция `convert()`

```python
def convert(markdown: str, *, wrap: str | None = None) -> str
```

Параметры:

- `markdown` — строка с markdown-текстом
- `wrap` — опциональная обёртка: `"container"`, `"container-fluid"` или `"row"`

## Поддерживаемые элементы Markdown

| Элемент          | Тег HTML     | Описание                     |
|------------------|--------------|------------------------------|
| Заголовки H1–H6   | `<h1>`–`<h6>`| Display-классы CoreUI        |
| Параграфы         | `<p>`        | Класс `mb-3`                 |
| Ссылки            | `<a>`        | Классы `text-primary` и др.  |
| Изображения       | `<img>`      | Класс `img-fluid`            |
| Строки кода       | `<code>`     | `text-monospace`, `bg-light` |
| Блоки кода        | `<pre>`      | Класс `highlight`            |
| Цитаты            | `<blockquote>` | Класс `blockquote`         |
| Списки            | `<ul>`, `<ol>` | Классы `list-unstyled`     |
| Элементы списков  | `<li>`       | Класс `mb-1`                 |
| Таблицы           | `<table>`    | Классы Bootstrap table       |
| Горизонтальные линии | `<hr>`   | Класс `my-4`                 |
| Сноски            |              | Классы `footnotes`, `badge`  |
| Task lists        |              | Классы `form-check-*`        |

## CSS-классы CoreUI

| Ключ       | CSS-классы                              |
|------------|-----------------------------------------|
| `h1`       | `display-4 mb-4`                        |
| `h2`       | `display-5 mb-3`                        |
| `h3`       | `display-6 mb-3`                        |
| `h4`       | `h4 mb-3`                               |
| `h5`       | `h5 mb-2`                               |
| `h6`       | `h6 mb-2`                               |
| `p`        | `mb-3`                                  |
| `a`        | `text-primary text-decoration-none`     |
| `img`      | `img-fluid rounded`                     |
| `blockquote` | `blockquote`                          |
| `pre`      | `highlight mb-3`                       |
| `table`    | `table table-striped table-hover`       |
| `hr`       | `my-4`                                  |
| `ul/ol`    | `list-unstyled ps-3`                    |

## Примеры

### Простой Markdown → HTML

```python
from md2coreui import convert

md = "## Заголовок\n\nЭто текст параграфа."
html = convert(md)
# <h2 class="display-5 mb-3">Заголовок</h2>
# <p class="mb-3">Это текст параграфа.</p>
```

### С обёрткой container

```python
html = convert("# Заголовок", wrap="container")
# <div class="container">
#   <h1 class="display-4 mb-4">Заголовок</h1>
# </div>
```

### С обёрткой container-fluid

```python
html = convert("# Заголовок", wrap="container-fluid")
# <div class="container-fluid">
#   <h1 class="display-4 mb-4">Заголовок</h1>
# </div>
```

### С обёрткой row

```python
html = convert("# Заголовок", wrap="row")
# <div class="row">
#   <h1 class="display-4 mb-4">Заголовок</h1>
# </div>
```
