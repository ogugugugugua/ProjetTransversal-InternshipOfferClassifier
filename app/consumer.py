import persistqueue

class Consumer:
    def __init__(self, feed_hyperplan):
        self.feeder = feed_hyperplan
        self.q = persistqueue.SQLiteQueue('queue', auto_commit=True)
    def consume(self):
        while True:
            text = self.q.get()
            print(text)