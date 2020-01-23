from feed_hyperplan import FeedHyperplan
from consumer import Consumer

feeder = FeedHyperplan()
feeder.classify(0, "machine")

# consumer = Consumer(feeder)
# consumer.consume()