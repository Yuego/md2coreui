from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

from md2coreui._classes import CLASSES

TAG_TO_KEY = {
    "h1": "h1",
    "h2": "h2",
    "h3": "h3",
    "h4": "h4",
    "h5": "h5",
    "h6": "h6",
    "p": "p",
    "a": "a",
    "img": "img",
    "blockquote": "blockquote",
    "code": "code_inline",
    "pre": "pre",
    "table": "table",
    "thead": "thead",
    "th": "th",
    "hr": "hr",
    "ul": "ul",
    "ol": "ol",
    "li": "li",
}


class _CssTreeprocessor(Treeprocessor):
    def __init__(self, md, class_map: dict[str, str]):
        super().__init__(md)
        self.class_map = class_map

    def run(self, root):
        for el in root.iter():
            tag = el.tag
            key = TAG_TO_KEY.get(tag)
            if key and key in self.class_map:
                existing = el.get("class", "")
                css_class = self.class_map[key]
                if css_class not in existing:
                    el.set("class", f"{existing} {css_class}".strip())
        return None


class CoreUICssClassesExtension(Extension):
    def __init__(self, class_map: dict[str, str] | None = None, **kwargs):
        self.config = {
            "class_map": [
                {k: v for k, v in CLASSES.items() if k in TAG_TO_KEY.values()},
                "Mapping of element keys to CSS classes",
            ],
        }
        super().__init__(**kwargs)
        if class_map is not None:
            self.setConfig("class_map", class_map)

    def extendMarkdown(self, md):
        class_map = self.getConfig("class_map")
        processor = _CssTreeprocessor(md, class_map)
        md.treeprocessors.register(processor, "coreui_css_classes", 25)


def makeExtension(**kwargs):
    return CoreUICssClassesExtension(**kwargs)
