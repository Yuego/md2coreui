from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor


class _TableWrapPostprocessor(Postprocessor):
    def run(self, text: str) -> str:
        text = text.replace(
            "<table",
            '<div class="table-responsive"><table',
        )
        text = text.replace(
            "</table>",
            "</table></div>",
        )
        return text


class CoreUITableWrapExtension(Extension):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        md.postprocessors.register(
            _TableWrapPostprocessor(md),
            "coreui_table_wrap",
            30,
        )


def makeExtension(**kwargs):
    return CoreUITableWrapExtension(**kwargs)
