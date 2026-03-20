def wrap_container(html: str, *, fluid: bool = False) -> str:
    cls = "container-fluid" if fluid else "container"
    return f'<div class="{cls}">{html}</div>'


def wrap_row(html: str) -> str:
    return f'<div class="row">{html}</div>'
