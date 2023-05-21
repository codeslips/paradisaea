from ninja import NinjaAPI
from file.api import router as  FileRouter
from knowledge.api import router as KnowRouter
from note.api import router as NoteRouter
from todo.api import router as TodoRouter
from chat.api import router as ChatRouter


api = NinjaAPI(urls_namespace="api",title="Paradisae Basic Api")

api.add_router("/file", FileRouter,tags=["file"])
api.add_router("/know", KnowRouter,tags=["know"])
api.add_router("/note", NoteRouter,tags=["note"])
api.add_router("/todo", TodoRouter,tags=["todo"])
api.add_router("/chat", ChatRouter,tags=["chat"])
