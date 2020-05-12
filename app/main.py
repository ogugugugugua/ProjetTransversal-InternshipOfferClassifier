from feed_hyperplan import FeedHyperplan
from consumer import Consumer
import sys
from utils import abs_path
from algorithms.tf_idf_heuristic import classifier
import time

"""Script principal, attente de l'arrivée d'offres dans la queue."""

sys.path.insert(0, abs_path("algorithms/multinomial_nb_sklearn"))
# print(sys.path)

feeder = FeedHyperplan()
# feeder.benchmark(1000)

t_begin = time.process_time()
for i in range(1000):
    classifier.predict("test")

t_end = time.process_time()
print("Temps execution (s): ", t_end - t_begin)

# consumer = Consumer(feeder)
# consumer.consume()