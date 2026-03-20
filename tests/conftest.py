import pytest


@pytest.fixture
def sample_h1():
    return "# Заголовок H1"


@pytest.fixture
def sample_h2():
    return "## Заголовок H2"


@pytest.fixture
def sample_paragraph():
    return "Это параграф текста."


@pytest.fixture
def sample_list():
    return "- элемент 1\n- элемент 2\n- элемент 3"


@pytest.fixture
def sample_ordered_list():
    return "1. Первый\n2. Второй\n3. Третий"


@pytest.fixture
def sample_code_inline():
    return "Это `inline code` в тексте."


@pytest.fixture
def sample_code_block():
    return "```python\nprint('Hello')\n```"


@pytest.fixture
def sample_blockquote():
    return "> Это цитата"


@pytest.fixture
def sample_table():
    return "| Заголовок 1 | Заголовок 2 |\n|-------------|-------------|\n| Ячейка 1    | Ячейка 2    |"


@pytest.fixture
def sample_link():
    return "[Ссылка](https://example.com)"


@pytest.fixture
def sample_image():
    return "![Alt text](https://example.com/image.png)"


@pytest.fixture
def sample_task_list():
    return "- [ ] Не выполнено\n- [x] Выполнено"


@pytest.fixture
def sample_hr():
    return "---\n\nТекст после hr"


@pytest.fixture
def sample_footnote():
    return "Текст со сноской[^1]\n\n[^1]: Текст сноски"
