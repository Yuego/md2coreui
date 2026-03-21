import pytest

mistune = pytest.importorskip("mistune")
from md2coreui import convert
from md2coreui._classes import CLASSES


class TestHeadings:
    def test_h1(self, sample_h1):
        html = convert(sample_h1)
        assert "display-4" in html
        assert "<h1" in html

    def test_h2(self, sample_h2):
        html = convert(sample_h2)
        assert "display-5" in html
        assert "<h2" in html


class TestParagraph:
    def test_paragraph(self, sample_paragraph):
        html = convert(sample_paragraph)
        assert "mb-3" in html
        assert "<p" in html


class TestLists:
    def test_unordered_list(self, sample_list):
        html = convert(sample_list)
        assert "list-unstyled" in html
        assert "<ul" in html

    def test_ordered_list(self, sample_ordered_list):
        html = convert(sample_ordered_list)
        assert "list-unstyled" in html
        assert "<ol" in html


class TestCode:
    def test_inline_code(self, sample_code_inline):
        html = convert(sample_code_inline)
        assert "text-monospace" in html
        assert "<code" in html

    def test_code_block(self, sample_code_block):
        html = convert(sample_code_block)
        assert "highlight" in html
        assert "language-python" in html
        assert "<pre" in html


class TestBlockquote:
    def test_blockquote(self, sample_blockquote):
        html = convert(sample_blockquote)
        assert "blockquote" in html
        assert "<blockquote" in html


class TestTable:
    def test_table(self, sample_table):
        html = convert(sample_table)
        assert "table table-striped table-hover" in html
        assert "<table" in html
        assert "table-responsive" in html


class TestLinks:
    def test_link(self, sample_link):
        html = convert(sample_link)
        assert "text-primary" in html
        assert "<a" in html


class TestImages:
    def test_image(self, sample_image):
        html = convert(sample_image)
        assert "img-fluid" in html
        assert "<img" in html


class TestTaskList:
    def test_task_list(self, sample_task_list):
        html = convert(sample_task_list)
        assert "task-list-item" in html or "form-check" in html


class TestHorizontalRule:
    def test_hr(self, sample_hr):
        html = convert(sample_hr)
        assert "my-4" in html
        assert "<hr" in html


class TestFootnotes:
    def test_footnote(self, sample_footnote):
        html = convert(sample_footnote)
        assert "footnotes" in html
        assert "badge" in html


class TestWrapper:
    def test_wrap_container(self):
        html = convert("# Test", wrap="container")
        assert '<div class="container">' in html
        assert "</div>" in html

    def test_wrap_container_fluid(self):
        html = convert("# Test", wrap="container-fluid")
        assert '<div class="container-fluid">' in html

    def test_wrap_row(self):
        html = convert("# Test", wrap="row")
        assert '<div class="row">' in html
        assert "</div>" in html
