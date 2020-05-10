import os
import time
import persistqueue
import random

class FeedHyperplan:

    def __init__(self):
        self.list = ["intelligence artificielle", "v2x", "developpeur web api",
            "developpeur stm32", "ingenieur architecture web",
            "Technicien informatique H/F", "technicien informatique d’exploitation INDRET (H/F)",
            "Testeur Informatique", "Developpeur web full stack H/F",
            "Collaborateur comptable H/F", "Technicien(ne) maintenance informatique",
            "Developpeur PHP Back Office", "Developpeur Front-end Angular/NodeJS/Javascript",
            "Tech lead Full Stack Java", "Stage Developpeur Web Javascript"]

    def feed(self):
        q = persistqueue.SQLiteQueue(os.path.join(os.path.dirname(__file__), "../queue"), auto_commit=True)
        for i in range(100):
            q.put({"id": i, "clean_text": random.choice(self.list)})

    def MesureTemps(self):
        startTime = time.time()
        self.feed()
        endTime = time.time()
        print (endTime - startTime)


if __name__ == '__main__':
    feedHyperplan = FeedHyperplan()
    feedHyperplan.MesureTemps()