from bottle import route,run

@route("/")
def index():
    return"""
    <h2>Verkefni 1</h1>
    <a href="/about">About</a>
    <a href="/bio"> biography</a>
    <a href="/pic">Pictures</a>
    """

@route("/about")
def jobs():
    return "Hér eru uplýsinger um steve jobs"

@route("/bio")
def jobs():
    return "Hér er biograpy frá steve jobs"

@route("/pic")
def jobs():
    return "Hér eru myndir frá lifi steve jobs"

run(host='localhost', port=8080,debug=True)


