from feed_hyperplan import FeedHyperplan
from consumer import Consumer

feeder = FeedHyperplan()

consumer = Consumer(feeder)
consumer.consume()

consumer.writer.close()