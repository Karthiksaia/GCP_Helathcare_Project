winners = ["Alice", "Bob", "Charlie", "Charlie", "Bob"]
scoreboard_counts = {}
for winner in winners:
    if winner in scoreboard_counts:
        scoreboard_counts[winner] += 1
    else:
        scoreboard_counts[winner] = 1
print(scoreboard_counts)


#added chanegs by sc