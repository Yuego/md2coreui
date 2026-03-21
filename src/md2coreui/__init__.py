from ._classes import CLASSES


def _get_wrap_fns():
    from .mistune._wrapper import wrap_container, wrap_row

    return wrap_container, wrap_row


def convert(markdown_text, *, engine="mistune", wrap=None, **kwargs):
    if engine == "mistune":
        try:
            import mistune
            from .mistune import create_renderer
        except ImportError:
            raise ImportError(
                "The 'mistune' package is required for engine='mistune'. "
                "Install it with: pip install md2coreui[mistune]"
            )
        renderer = create_renderer()
        md = mistune.create_markdown(
            renderer=renderer, plugins=["table", "task_lists", "footnotes"]
        )
        html = md(markdown_text)
    elif engine == "markdown":
        from .markdown import convert as _md_convert

        html = _md_convert(markdown_text, **kwargs)
    else:
        raise ValueError(f"Unknown engine: {engine!r}. Use 'mistune' or 'markdown'.")

    if wrap is not None:
        wrap_container, wrap_row = _get_wrap_fns()
        if wrap == "container":
            html = wrap_container(html)
        elif wrap == "container-fluid":
            html = wrap_container(html, fluid=True)
        elif wrap == "row":
            html = wrap_row(html)
    return html


def wrap_container(html, *, fluid=False):
    from .mistune._wrapper import wrap_container as _wrap

    return _wrap(html, fluid=fluid)


def wrap_row(html):
    from .mistune._wrapper import wrap_row as _wrap

    return _wrap(html)


__all__ = [
    "convert",
    "wrap_container",
    "wrap_row",
    "CLASSES",
]
