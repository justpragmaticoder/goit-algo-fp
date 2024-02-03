import random
from collections import Counter


def throw_dice():
    return random.randint(1, 6)


def simulate(num_trials):
    results = Counter()

    for _ in range(num_trials):
        dice1 = throw_dice()
        dice2 = throw_dice()
        total = dice1 + dice2
        results[total] += 1

    probabilities = {key: value / num_trials * 100 for key, value in results.items()}

    return probabilities


def print_probabilities(probabilities):
    print("Summ\tProbability")
    for total, probability in probabilities.items():
        print(f"{total}\t{probability:.2f}% ({results[total]}/{num_trials})")


if __name__ == "__main__":
    num_trials = 100000
    results = simulate(num_trials)
    print_probabilities(results)
