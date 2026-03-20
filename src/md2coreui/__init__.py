import mistune
from ._renderer import create_renderer, MistuneRenderer
from ._wrapper import wrap_container, wrap_row
from ._classes import CLASSES


def convert(markdown: str, *, wrap: str | None = None) -> str:
    renderer = create_renderer()
    md = mistune.create_markdown(
        renderer=renderer, plugins=["table", "task_lists", "footnotes"]
    )
    html = md(markdown)
    if wrap == "container":
        html = wrap_container(html)
    elif wrap == "container-fluid":
        html = wrap_container(html, fluid=True)
    elif wrap == "row":
        html = wrap_row(html)
    return html


__all__ = [
    "convert",
    "wrap_container",
    "wrap_row",
    "CLASSES",
    "MistuneRenderer",
    "create_renderer",
]
