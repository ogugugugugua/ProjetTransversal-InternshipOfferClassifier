from feed_hyperplan import FeedHyperplan
from consumer import Consumer
import sys
from utils import abs_path

sys.path.insert(0, abs_path("algorithms/multinomial_nb_sklearn"))
# print(sys.path)

feeder = FeedHyperplan()
# feeder.classify(0, "machine")

consumer = Consumer(feeder)
consumer.consume()