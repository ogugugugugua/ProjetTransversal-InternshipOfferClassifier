import os
import time
import persistqueue

class FeedHyperplan:

    def feed(self):
        q = persistqueue.SQLiteQueue(os.path.join(os.path.dirname(__file__), "../queue"), auto_commit=True)
        for i in range(100):
            q.put({"id": 0, "clean_text": "intelligence artificielle"})
            q.put({"id": 1, "clean_text": "v2x"})
            q.put({"id": 2, "clean_text": "developpeur web api"})

    def MesureTemps(self):
        startTime = time.time()
        self.feed()
        endTime = time.time()
        print (endTime - startTime)


if __name__ == '__main__':
    feedHyperplan = FeedHyperplan()
    feedHyperplan.MesureTemps()