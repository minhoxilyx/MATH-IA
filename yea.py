import random

def draw_card():
    card = random.choice([2,3,4,5,6,7,8,9,10,10,10,10,11])
    return card

def hand_value(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10  # Convert A from 11 → 1
        aces -= 1
    return total

def dealer_turn(h17=True):
    hand = [draw_card(), draw_card()]
    total = hand_value(hand)

    while True:
        soft = (11 in hand and total <= 21)
        if total < 17:
            hand.append(draw_card())
        elif total == 17 and h17 and soft:
            # hits on soft 17 if h17=True
            hand.append(draw_card())
        else:
            break
        total = hand_value(hand)

    return total

def simulate(player_total, h17=True, n_trials=100000):
    wins = 0
    ties = 0
    losses = 0

    for _ in range(n_trials):
        dealer_total = dealer_turn(h17)
        if dealer_total > 21:
            wins += 1
        elif dealer_total > player_total:
            losses += 1
        elif dealer_total == player_total:
            ties += 1
        else:
            wins += 1

    win_rate = wins / n_trials * 100
    loss_rate = losses / n_trials * 100
    tie_rate = ties / n_trials * 100

    return win_rate, loss_rate, tie_rate

for rule in [("S17", False), ("H17", True)]:
    print(f"\nDealer Rule: {rule[0]}")
    for player_total in [18, 19, 20]:
        win, loss, tie = simulate(player_total, h17=rule[1])
        print(f"Player {player_total}: Win={win:.2f}%, Loss={loss:.2f}%, Tie={tie:.2f}%")
