from Abstraction_functions import simple, identity, naive, possible, advanced, adv_hand, adv_hist, simple_hand
import wandb
from Experiment_functions import full_abstraction, abstraction_func
import argparse

"""This is the program, used for the Abstraction experiments."""

# Default constants
suits = 3
ranks = 3
hand_size = 3
train_iterations = 100000
intervals = 1000
eval_iterations = 20000
abstraction = "sim_hand"
FLAGS = None

def main():
    abstraction_functions = {
        "adv": advanced,
        "sim": simple,
        "naive": naive,
        "hand": adv_hand,
        "hist": adv_hist,
        "sim_hand": simple_hand
    }
    abstraction_func(FLAGS.suits, FLAGS.ranks, FLAGS.hand_size, FLAGS.train_iterations,
                     FLAGS.intervals, FLAGS.eval_iterations, abstraction_functions[FLAGS.abstraction])


if __name__ == '__main__':

    wandb.init(project='thesis', group='abstraction')
    config = wandb.config

    # Command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--suits', type=int, default=suits,
                        help='Number of suits')
    parser.add_argument('--ranks', type=int, default=ranks,
                        help='Number of ranks')
    parser.add_argument('--hand_size', type=int, default=hand_size,
                        help='Number of cards in a hand')
    parser.add_argument('--train_iterations', type=int, default=train_iterations,
                        help='Number of total train iterations')
    parser.add_argument('--intervals', type=int, default=intervals,
                        help='Frequency of evaluation')
    parser.add_argument('--eval_iterations', type=int, default=eval_iterations,
                        help='Number of iterations for evaluation')
    parser.add_argument('--abstraction', type=str, default=abstraction,
                        help='Abstraction type')
    FLAGS, unparsed = parser.parse_known_args()
    config.update(FLAGS)

    main()
