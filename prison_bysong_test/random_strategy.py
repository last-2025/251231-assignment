import random

def simulate_round_random(num_prisoners: int = 100, picks: int = 50, rng: random.Random | None = None) -> bool:
    """
    Random strategy:
    Each prisoner opens `picks` random distinct drawers (not using any info).
    Returns True iff ALL prisoners succeed in this round.
    """
    rng = rng or random
    drawers = list(range(num_prisoners))
    rng.shuffle(drawers)

    indices = list(range(num_prisoners))
    for prisoner in range(num_prisoners):
        found = False
        for idx in rng.sample(indices, picks):
            if drawers[idx] == prisoner:
                found = True
                break
        if not found:
            return False
    return True


def play_random(trials: int = 100_000, num_prisoners: int = 100, picks: int = 50, seed: int | None = None) -> float:
    """
    Returns win rate (%) over `trials`.
    """
    rng = random.Random(seed)
    wins = sum(simulate_round_random(num_prisoners, picks, rng) for _ in range(trials))
    return wins / trials * 100.0

