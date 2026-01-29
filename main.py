#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# tt_thoma
# I keep forgetting how flask works
import traceback

# Global imports
import flask
import flask_ipban
import json
import os
import werkzeug.exceptions

app = flask.Flask(
    __name__
)

ip_ban = flask_ipban.IpBan(
    ban_count=3,
    ban_seconds=3600*24,  # 24 hours
    persist=True,
    record_dir="../ipban_records",
    ipc=True,
)
ip_ban.init_app(app)
ip_ban.load_nuisances()

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/reader/")
def reader_base():
    return flask.redirect("/reader/home/")

@app.route("/reader/<page>/")
def reader_page(page):
    if not os.path.exists(f"blog/{page}.json"):
        flask.abort(404)

    with open(f"blog/{page}.json", "r", encoding="utf-8") as json_f:
        data = json.load(json_f)

    with open(f"blog/{page}.html", "r", encoding="utf-8") as html_f:
        content = html_f.read()

    return flask.render_template(
        "reader.html",
        splash="So retro! "*20,
        title=data["name"],
        content=content
    )

@app.route("/blog/<page>/page/")
def blog(page):
    return flask.send_from_directory("blog", f"{page}.html")

@app.route("/blog/<page>/")
def blog_title(page):
    return flask.send_from_directory("blog", f"{page}.json")

@app.route("/favicon.ico")
def favicon_ico():
    return flask.send_file("favicon.ico", mimetype="image/x-icon")

@app.route("/robots.txt")
def robots_txt():
    return flask.send_file("robots.txt", mimetype="text/plain")

@app.errorhandler(Exception)
def handle_exception(e):
    if flask.request.endpoint == "reader_page":
        if isinstance(e, werkzeug.exceptions.HTTPException):
            code = e.code
            description = e.get_description().strip()
        else:
            print(traceback.format_exc())
            code = 500
            description = (
                "The server encountered an internal error and was unable to complete your request."
                "Either the server is overloaded or there is an error in the application."
            )

        return flask.render_template(
            "reader.html",
            splash="So retro! " * 20,
            title=f"{code}",
            content=f"<h1>Oops!... :&lt;</h1>\n{description}",
        )

    if isinstance(e, werkzeug.exceptions.HTTPException):
        return e

    print(traceback.format_exc())
    return werkzeug.exceptions.InternalServerError()

if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=80)
