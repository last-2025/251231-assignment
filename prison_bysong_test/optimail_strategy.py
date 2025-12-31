import random

def simulate_round_optimal(num_prisoners: int = 100, picks: int = 50, rng: random.Random | None = None) -> bool:
    """
    Optimal (cycle-following) strategy:
    Prisoner starts at their own index, then follows the number found.
    Returns True iff ALL prisoners succeed in this round.
    """
    rng = rng or random
    drawers = list(range(num_prisoners))
    rng.shuffle(drawers)

    for prisoner in range(num_prisoners):
        reveal = prisoner
        for _ in range(picks):
            card = drawers[reveal]
            if card == prisoner:
                break
            reveal = card
        else:
            return False
    return True


def play_optimal(trials: int = 100_000, num_prisoners: int = 100, picks: int = 50, seed: int | None = None) -> float:
    """
    Returns win rate (%) over `trials`.
    """
    rng = random.Random(seed)
    wins = sum(simulate_round_optimal(num_prisoners, picks, rng) for _ in range(trials))
    return wins / trials * 100.0

