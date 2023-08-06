import bleach
import markdown
from . import config


def render_markdown(content: str) -> str:
    return bleach.clean(markdown.markdown(
        content,
        extensions=config.markdown_extensions
    ),
        tags=bleach.ALLOWED_TAGS + config.markdown_extra_tags,
        attributes={**bleach.ALLOWED_ATTRIBUTES, **config.markdown_extra_attrs}
    )
