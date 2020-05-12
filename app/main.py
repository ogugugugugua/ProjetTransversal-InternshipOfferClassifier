from feed_hyperplan import FeedHyperplan
from consumer import Consumer
import sys
from utils import abs_path

"""Script principal, attente de l'arrivée d'offres dans la queue."""

sys.path.insert(0, abs_path("algorithms/multinomial_nb_sklearn"))
# print(sys.path)

feeder = FeedHyperplan()
feeder.benchmark(1000)

# consumer = Consumer(feeder)
# consumer.consume()