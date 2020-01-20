from feed_hyperplan import FeedHyperplan
from consumer import Consumer

feeder = FeedHyperplan()
feeder.classify("machine")

# consumer = Consumer(feeder)
# consumer.consume()

# consumer.writer.close()