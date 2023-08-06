import datetime
import functools
import io
import itertools
import json
import os
import random
import string

import flask
from flask import Blueprint, render_template, request, abort, Response, url_for, send_from_directory
import PIL.Image as pil_image
from werkzeug.utils import secure_filename

from . import config, render
from . import dataclasses
from . import fragments

cms = Blueprint(
    'simple_flask_cms',
    '__name__',
    static_folder=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static'),
    template_folder=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates'),
    url_prefix='/cms'
)


def require_authentication(func):
    assert func.__name__ in config.viewer_paths or func.__name__ in config.editor_paths

    @functools.wraps(func)
    def _inner(*args, **kwargs):
        result = config.authentication_function(
            action=func.__name__,
            parameters=kwargs
        )
        if result is not None:
            return result

        return func(*args, **kwargs)

    return _inner


def generate_nav(pages):
    pages = list(itertools.chain(pages, config.extra_nav_urls))
    pages.sort(key=lambda i: i.path)
    nav = []
    page_stack = []
    page_name_stack = []

    for page in pages:
        page.subpages = []
        parts = page.path.split('/')
        max_index = 0
        for index, (path_variable, part_variable) in enumerate(zip(page_name_stack, parts)):
            if path_variable != part_variable:
                break

            max_index = index + 1
        del page_stack[max_index:]
        del page_name_stack[max_index:]

        if len(page_stack) == 0:
            assert max_index == 0
            nav.append(page)
        else:
            assert max_index != 0
            page_stack[-1].subpages.append(page)
            page_stack[-1].subpages.sort(key=lambda i: i.sort_order)

        if len(parts) > max_index:
            page_name_stack.extend(parts[max_index:])
            assert len(page_name_stack) == len(parts)
            while len(page_stack) < len(parts) - 1:
                if len(page_stack) >= 1:
                    page_stack.append(page_stack[-1])
                else:
                    # No suitable page found, whatever
                    page_stack.append(page)
            page_stack.append(page)

    nav.sort(key=lambda i: i.sort_order)
    return nav


@cms.route("editor")
@cms.route("editor/")
@require_authentication
def editor_home():
    nrof_pages = config.db_connection.get_nrof_pages()
    nrof_images = config.db_connection.get_nrof_images()

    return render_template("cms/overview.html", nrof_pages=nrof_pages, nrof_images=nrof_images,
                           fragments=config.fragments, nav=nav
                           )


@cms.route("editor/admin/<path:path>", methods=["POST"])
@require_authentication
def delete_page(path):
    page = config.db_connection.get_page(path)
    if page is None:
        abort(404)
    # Check if it's valid JSON as a CSRF protection mechanism
    if not request.is_json:
        abort(400)
    page.json()

    config.db_connection.delete_page(path)

    return Response('{}', headers={'Content-Type': 'Application/JSON'})


@cms.route("admin/images", methods=["POST"])
@require_authentication
def upload_image():
    page = str(request.headers.get("X-Page"))[:50]
    if not page:
        return "Invalid page", 400
    content_type = request.content_type
    if content_type not in image_content_types:
        return "Invalid Image", 400

    data = io.BytesIO(request.get_data(as_text=False))

    # Make sure the file is a valid image, recognized by PIL
    image = pil_image.open(data)
    image.load()

    filename = secure_filename(request.headers.get("X-Filename", '')).replace('.', '')
    if not filename:
        return "Invalid Request", 400
    filename += '.webp'  # mimetypes.guess_extension(content_type, False)

    while os.path.isfile(os.path.join(config.upload_folder, filename)):
        filename = random.choice(string.ascii_lowercase) + filename

    image.save(os.path.join(config.upload_folder, filename), 'webp')
    # with open(os.path.join(config.upload_folder, filename), 'wb') as f:
    #    data.seek(0)
    #    f.write(data.read())

    config.db_connection.save_image(
        dataclasses.Image(
            file=filename,
            page=page,
            mime_type=content_type,
            size=data.getbuffer().nbytes
        )
    )

    return Response(
        json.dumps({
            "path": url_for("simple_flask_cms.get_image", path=filename),
            "filename": filename
        })
    )


@cms.route("editor/images/list")
@require_authentication
def list_images():
    images = list(config.db_connection.get_all_images())
    for image in images:
        if image.page.startswith('#fragment:'):
            image.page = url_for(
                'simple_flask_cms.fragment',
                name=image.page[len('#fragment:'):]
            )
        else:
            image.page = url_for(
                'simple_flask_cms.editor',
                path=image.page
            )

    return render_template('cms/images.html', images=images, nav=nav, fragments=config.fragments)


@cms.route('/editor/<path:path>', methods=['GET', 'POST'])
@require_authentication
def editor(path):
    pages = list(config.db_connection.get_all_pages())

    if request.method == 'POST':
        data = request.json

        if data is None:
            return 'Invalid JSON', 400

        post = dataclasses.Page(
            **data,
            date_modified=datetime.datetime.utcnow(),
            path=path
        )

        config.db_connection.save_page(post)

    nav[:] = generate_nav(pages)

    images = config.db_connection.get_images_for_page(path)

    page = config.db_connection.get_page(path)

    return render_template("cms/editor.html", nav=nav, current_page=page, url=path, images=images,
                           fragments=config.fragments)


@cms.route('editor/admin/fragments/<string:name>', methods=["GET", "POST"])
@require_authentication
def fragment(name):
    if name not in fragments_map:
        abort(404)

    if flask.request.method == "POST":
        if not flask.request.is_json:
            return "Bad request", 400

        data = flask.request.json

        frag = dataclasses.Fragment(
            content=data.get("content"),
            name=name,
            date_modified=datetime.datetime.now()
        )

        config.db_connection.save_fragment(frag)

        return flask.Response(
            '{}',
            headers={
                'Content-Type': 'Application/JSON'
            }
        )

    frag = config.db_connection.get_fragment(name)
    if frag is None:
        frag = dataclasses.Fragment(
            name=name,
            content="",
            date_modified=datetime.datetime.now()
        )
    frag.fragment_type = fragments_map[frag.name]

    images = config.db_connection.get_images_for_page('#fragment:' + name)
    return render_template("cms/fragment.html", nav=nav, fragment=frag, images=images, fragments=config.fragments)


@cms.route("admin/images/delete/<string:filename>", methods=["POST"])
@require_authentication
def delete_image(filename):
    filename = secure_filename(filename)
    if not os.path.isfile(os.path.join(config.upload_folder, filename)):
        return "File not found", 400

    image = config.db_connection.get_image(filename)

    if image is None:
        return "File not in database", 400

    os.unlink(os.path.join(os.path.join(config.upload_folder, filename)))
    config.db_connection.delete_image(
        filename
    )

    return "deleted", 200


@cms.route("images/<string:path>")
@require_authentication
def get_image(path):
    return send_from_directory(config.upload_folder, path)


@cms.route("<path:path>")
@require_authentication
def page(path):
    use_json = False
    if request.headers.get("Accept") == "Application/JSON":
        use_json = True
    elif path.endswith('.json'):
        use_json = True
        path = path.split('.')[0]
    page = config.db_connection.get_page(path)

    if page is None:
        if config.enable_custom_404:
            return render_template(
                'cms/404.html',
                path=path
            ), 404
        else:
            abort(404)

    if not use_json or request.headers.get('X-IncludeHTML', 'true').lower() != 'false':
        page.html = render.render_markdown(page.content)
    if use_json and request.headers.get('X-IncludeMarkdown', 'true').lower() == 'false':
        page.content = ""

    if use_json:
        return flask.Response(
            json.dumps({
                "page": json.loads(page.json()),
                "nav": [json.loads(i.json()) for i in nav]
            }),
            headers={
                "Content-Type": "Application/JSON"
            }
        )

    return render_template(
        config.template_name,
        page=page,
        nav=nav,
        **config.extra_page_content_provider(path)
    )


@cms.before_app_first_request
def build_initial_nav():
    if config.db_connection is None:
        raise ValueError("Set a database before starting the CMS")

    pages = config.db_connection.get_all_pages()
    nav[:] = generate_nav(pages)
    for fragment in config.fragments:
        fragments_map[fragment.name] = fragment

    if not os.path.isdir(config.upload_folder):
        raise ValueError(
            f"The folder {config.upload_folder!r} does not exist. Please create the folder or set the"
            f" `simple_flask_cms.upload_folder` config variable to the folder you want to upload media to")


@cms.app_template_global("cms_fragment")
def cms_fragment(name):
    return fragments.get_fragment(name).html


@cms.app_template_global("cms_nav")
def cms_nav():
    return nav


nav = []
fragments_map = {}

image_content_types = [
    'image/jpeg',
    'image/jpg',
    'image/png',
    'application/png',
    'image/webp',
    'image/gif',
    'image/tif',
    'image/tiff',
]
