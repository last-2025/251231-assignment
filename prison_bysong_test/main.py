from random_strategy import play_random
from optimal_strategy import play_optimal

def main():
    trials = 100_000
    print("Simulation count:", trials)
    print(f"Random play wins : {play_random(trials):4.1f}% of simulations")
    print(f"Optimal play wins: {play_optimal(trials):4.1f}% of simulations")

if __name__ == "__main__":
    main()

