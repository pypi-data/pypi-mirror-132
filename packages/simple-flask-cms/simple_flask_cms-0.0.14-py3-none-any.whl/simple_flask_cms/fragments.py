from . import config
from . import render
from . import dataclasses
import datetime


def get_fragment(name, include_html=True, include_markdown=False) -> dataclasses.Fragment:
    fragment = config.db_connection.get_fragment(name)
    if fragment is None:
        return dataclasses.Fragment(
            name=name,
            date_modified=datetime.datetime(year=1975, month=1, day=1),
            html="",
            content="",
        )
    if include_html:
        fragment.html = render.render_markdown(fragment.content)
    if not include_markdown:
        fragment.content = ""
    return fragment
