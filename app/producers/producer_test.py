import persistqueue
import os

q = persistqueue.SQLiteQueue(os.path.join(os.path.dirname(__file__), "../queue"), auto_commit=True)
q.put({"id": 0, "clean_text": "intelligence artificielle"})
q.put({"id": 1, "clean_text": "v2x"})
q.put({"id": 2, "clean_text": "developpeur web api"})