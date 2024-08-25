from databases import Database
from quart import Quart

app = Quart(__name__)
app.config.update({
    "DATABASE_URL": "postgresql://todo:@localhost:5432/todo"
})

@app.route("/")
async def index() -> str:
    return "hi"

async def _create_db_connection() -> Database:
    db = Database(app.config["DATABASE_URL"])
    await db.connect()
    return db