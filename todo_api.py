from quart import Quart

app = Quart(__name__)

@app.route("/")
async def index() -> str:
    return "hi"

