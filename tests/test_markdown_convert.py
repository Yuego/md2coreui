import pytest

markdown_lib = pytest.importorskip("markdown")
from md2coreui import convert


class TestMarkdownEngine:
    def test_heading(self):
        html = convert("# Заголовок", engine="markdown")
        assert "display-4" in html
        assert "<h1" in html

    def test_paragraph(self):
        html = convert("Текст параграфа.", engine="markdown")
        assert "mb-3" in html
        assert "<p" in html

    def test_link(self):
        html = convert("[Ссылка](https://example.com)", engine="markdown")
        assert '<a href="https://example.com">Ссылка</a>' in html
        assert "<a" in html

    def test_image(self):
        html = convert("![Alt](https://example.com/img.png)", engine="markdown")
        assert '<img alt="Alt"' in html
        assert 'src="https://example.com/img.png"' in html
        assert "<img" in html

    def test_blockquote(self):
        html = convert("> Цитата", engine="markdown")
        assert "blockquote" in html
        assert "<blockquote" in html

    def test_inline_code(self):
        html = convert("Текст `code` текст", engine="markdown")
        assert "<code" in html
        assert "code" in html

    def test_code_block(self):
        md = "```python\nprint('hello')\n```"
        html = convert(md, engine="markdown", extensions=["fenced_code"])
        assert "<pre" in html
        assert "language-python" in html

    def test_unordered_list(self):
        md = "- элемент 1\n- элемент 2"
        html = convert(md, engine="markdown")
        assert "list-unstyled" in html
        assert "<ul" in html

    def test_ordered_list(self):
        md = "1. Первый\n2. Второй"
        html = convert(md, engine="markdown")
        assert "list-unstyled" in html
        assert "<ol" in html

    def test_table(self):
        md = "| A | B |\n|---|---|\n| 1 | 2 |"
        html = convert(md, engine="markdown", extensions=["tables"])
        assert "table" in html
        assert "table-responsive" in html

    def test_horizontal_rule(self):
        html = convert("---", engine="markdown")
        assert "my-4" in html
        assert "<hr" in html

    def test_h2(self):
        html = convert("## H2", engine="markdown")
        assert "display-5" in html
        assert "<h2" in html


class TestMarkdownEngineWrapping:
    def test_wrap_container(self):
        html = convert("# Test", engine="markdown", wrap="container")
        assert '<div class="container">' in html

    def test_wrap_container_fluid(self):
        html = convert("# Test", engine="markdown", wrap="container-fluid")
        assert '<div class="container-fluid">' in html

    def test_wrap_row(self):
        html = convert("# Test", engine="markdown", wrap="row")
        assert '<div class="row">' in html


class TestMistuneEngineDefault:
    def test_default_engine_is_mistune(self):
        mistune_lib = pytest.importorskip("mistune")
        html = convert("# Test")
        assert "<h1" in html

    def test_explicit_mistune(self):
        mistune_lib = pytest.importorskip("mistune")
        html = convert("# Test", engine="mistune")
        assert "<h1" in html


class TestInvalidEngine:
    def test_invalid_engine_raises(self):
        with pytest.raises(ValueError, match="Unknown engine"):
            convert("# Test", engine="invalid")
