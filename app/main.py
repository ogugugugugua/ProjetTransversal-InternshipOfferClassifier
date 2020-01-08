from feed_hyperplan import FeedHyperplan
from consumer import Consumer

feeder = FeedHyperplan()
# feeder.classify(feeder.extract_string_from_file("datasets/Stage EasyBroadcast 2019.pdf.txt"))

consumer = Consumer(feeder)
consumer.consume()