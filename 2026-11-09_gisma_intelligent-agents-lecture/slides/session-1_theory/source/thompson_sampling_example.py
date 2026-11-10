"""Reproduces the Thompson sampling example on slides 30-32 of Session 1.

Three slot machines start with some past results. Each machine's belief is Beta(alpha, beta)
with a flat prior Beta(1, 1), so alpha = 1 + wins and beta = 1 + losses.
Each turn: draw one sample (the ERP, estimated reward probability) from every machine's Beta,
play the machine with the highest draw, and add 1 to its alpha (win) or beta (loss).

The hidden true win rates are made up for the example; the agent never sees them.
Run: python3 thompson_sampling_example.py   (needs numpy)
"""
import numpy as np

SEED = 218
START = {'A': (2, 0), 'B': (6, 4), 'C': (1, 3)}   # (wins, losses) before the example
TRUE_P = {'A': 0.45, 'B': 0.65, 'C': 0.35}        # hidden; used only to simulate outcomes


def show(record, title):
    print(f'\n{title}')
    print(f'{"Machine":8}{"Wins":>6}{"Losses":>8}{"Raw":>8}{"Beta(a, b)":>14}{"a/(a+b)":>10}')
    for m, (w, l) in record.items():
        a, b = 1 + w, 1 + l
        print(f'{m:8}{w:>6}{l:>8}{w / (w + l):>8.0%}{f"Beta({a}, {b})":>14}{a / (a + b):>10.2f}')


rng = np.random.default_rng(SEED)
record = {m: list(v) for m, v in START.items()}
show(record, 'Before the five turns')
print()
for turn in range(1, 6):
    draws = {m: round(float(rng.beta(1 + w, 1 + l)), 2) for m, (w, l) in record.items()}
    pick = max(draws, key=draws.get)
    win = rng.random() < TRUE_P[pick]
    record[pick][0 if win else 1] += 1
    w, l = record[pick]
    print(f'Turn {turn}  ' + '  '.join(f'{m} {v:.2f}' for m, v in draws.items())
          + f'  -> play {pick} -> {"win " if win else "loss"}  {pick} -> Beta({1 + w}, {1 + l})')
show(record, 'After the five turns')
