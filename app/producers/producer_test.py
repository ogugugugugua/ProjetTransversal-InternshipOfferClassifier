import persistqueue
import os

q = persistqueue.SQLiteQueue(os.path.join(os.path.dirname(__file__), "../queue"), auto_commit=True)
q.put({"id": 0, "clean_text": "machine développeur"})
q.put({"id": 1, "clean_text": "développeur"})
q.put({"id": 2, "clean_text": "image"})