import mistune
from md2coreui._classes import CLASSES


class MistuneRenderer(mistune.HTMLRenderer):
    def heading(self, text: str, level: int, **attrs) -> str:
        cls = CLASSES.get(f"h{level}", "")
        return f'<h{level} class="{cls}">{text}</h{level}>\n'

    def paragraph(self, text: str) -> str:
        return f'<p class="{CLASSES["p"]}">{text}</p>\n'

    def link(self, text: str, url: str, title: str | None = None) -> str:
        # safe_url отбрасывает javascript:/vbscript:/data: при
        # allow_harmful_protocols=False (см. create_renderer ниже).
        safe_href = self.safe_url(url)
        title_attr = f' title="{mistune.escape(title)}"' if title else ""
        return f'<a href="{safe_href}" class="{CLASSES["a"]}"{title_attr}>{text}</a>'

    def image(self, text: str, url: str, title: str | None = None) -> str:
        safe_src = self.safe_url(url)
        alt_attr = f' alt="{mistune.escape(text)}"' if text else ""
        title_attr = f' title="{mistune.escape(title)}"' if title else ""
        return f'<img src="{safe_src}" class="{CLASSES["img"]}"{alt_attr}{title_attr}>'

    def codespan(self, text: str) -> str:
        return f'<code class="{CLASSES["code_inline"]}">{text}</code>'

    def block_code(self, code: str, info: str | None = None) -> str:
        lang_cls = f"language-{info}" if info else ""
        return f'<pre class="{CLASSES["pre"]} {lang_cls}"><code>{code}</code></pre>\n'

    def block_quote(self, text: str) -> str:
        return f'<blockquote class="{CLASSES["blockquote"]}">{text}</blockquote>\n'

    def list_item(self, text: str) -> str:
        return f'<li class="{CLASSES["li"]}">{text}</li>\n'

    def list(self, text: str, ordered: bool, **attrs) -> str:
        tag = "ol" if ordered else "ul"
        cls_key = "ol" if ordered else "ul"
        return f'<{tag} class="{CLASSES[cls_key]}">{text}</{tag}>\n'

    def table(self, text: str) -> str:
        return (
            f'<div class="table-responsive">'
            f'<table class="{CLASSES["table"]}">{text}</table>'
            f"</div>\n"
        )

    def table_head(self, text: str) -> str:
        return f'<thead class="{CLASSES["thead"]}">{text}</thead>\n'

    def table_body(self, text: str) -> str:
        return f"<tbody>{text}</tbody>\n"

    def table_row(self, text: str) -> str:
        return f"<tr>{text}</tr>\n"

    def table_cell(
        self, text: str, align: str | None = None, head: bool = False
    ) -> str:
        if head:
            return f'<th class="{CLASSES["th"]}">{text}</th>'
        return f"<td>{text}</td>"

    def thematic_break(self) -> str:
        return f'<hr class="{CLASSES["hr"]}">\n'

    def footnotes(self, text: str) -> str:
        return f'<div class="{CLASSES["footnote_block"]}">{text}</div>\n'

    def footnote_ref(self, key: str, index: int) -> str:
        return f'<span class="{CLASSES["footnote_ref"]}"><sup>[{index}]</sup></span>'

    def footnote_item(self, text: str, key: str, index: int) -> str:
        return f'<li class="mb-2">{text}</li>\n'

    def task_list_item(self, text: str, checked: bool = False) -> str:
        checkbox = (
            f'<input class="{CLASSES["task_list_checkbox"]}" '
            f'type="checkbox" disabled{" checked" if checked else ""}>'
        )
        label_cls = CLASSES["task_list_label"]
        checked_cls = "text-decoration-line-through text-muted" if checked else ""
        if text.startswith("<p>"):
            text = text.replace("<p>", f'<p class="{label_cls} {checked_cls}">', 1)
        else:
            text = f'<p class="{label_cls} {checked_cls}">{text}</p>'
        return f'<li class="{CLASSES["task_list_item"]}">{checkbox}{text}</li>\n'


def create_renderer() -> mistune.HTMLRenderer:
    # allow_harmful_protocols=False (default): mistune.safe_url() блокирует
    # javascript:/vbscript:/data: схемы. Раньше True пропускал XSS через
    # markdown-ссылки [click](javascript:alert(1)).
    # escape=False оставлен — наши *_renderer методы сами строят HTML и
    # должны экранировать атрибуты вручную (mistune.escape применяется в
    # link/image/etc).
    return MistuneRenderer(escape=False, allow_harmful_protocols=False)
