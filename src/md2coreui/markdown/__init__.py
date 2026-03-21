from .extensions import CoreUICssClassesExtension, CoreUITableWrapExtension


def convert(
    text: str,
    *,
    extensions: list | None = None,
    extension_configs: dict | None = None,
) -> str:
    try:
        import markdown as md_lib
    except ImportError:
        raise ImportError(
            "The 'markdown' package is required for engine='markdown'. "
            "Install it with: pip install md2coreui[markdown]"
        )

    all_extensions = [CoreUICssClassesExtension(), CoreUITableWrapExtension()]
    if extensions:
        all_extensions.extend(extensions)

    all_configs = {}
    if extension_configs:
        all_configs.update(extension_configs)

    return md_lib.markdown(
        text,
        extensions=all_extensions,
        extension_configs=all_configs,
        output_format="html5",
    )


__all__ = ["convert", "CoreUICssClassesExtension", "CoreUITableWrapExtension"]
