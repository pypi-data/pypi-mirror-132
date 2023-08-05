"""A decentralized social platform."""

from understory import web
from understory.apps import (cache, data, indieauth_client, indieauth_server,
                             jobs, micropub_server, microsub_server, owner,
                             search, sites, system, text_editor, text_reader,
                             tracker, webmention_endpoint, websub_endpoint)
from understory.web import tx

__all__ = ["app"]

app = web.application(
    __name__,
    db=True,
    mounts=(
        owner.app,
        jobs.app,
        sites.app,
        search.app,
        cache.app,
        data.app,
        system.app,
        tracker.app,
        indieauth_server.app,
        indieauth_client.app,
        webmention_endpoint.app,
        websub_endpoint.app,
        text_editor.app,
        text_reader.app,
        microsub_server.app,
        micropub_server.posts.app,
        micropub_server.media.app,
        micropub_server.content.app,
    ),
)


def template(handler, app):
    """Wrap response with site-wide template."""
    yield
    if tx.response.headers.content_type == "text/html" and tx.response.claimed:
        tx.response.body = app.view.template(tx.response.body)


app.wrappers.insert(0, template)


@app.wrap
def doctype_html(handler, app):
    """Add the HTML doctype to the response."""
    yield
    if tx.response.headers.content_type == "text/html" and tx.response.claimed:
        tx.response.body = "<!doctype html>" + str(tx.response.body)


@app.control("sign-in")
class SignIn:
    """"""

    def get(self):
        return_url = web.form(return_url="").return_url
        return app.view.sign_in(return_url)
