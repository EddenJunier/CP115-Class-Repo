num_rounds = int(input())
final_score = 0
rounds_processed = 0

for i in range (num_rounds):
    round_score = float(input())
    if round_score > 100:
        final_score += round_score + (round_score * 0.2)
        rounds_processed += 1
    else:
        final_score += round_score
        rounds_processed += 1

print(f"{final_score:.1f}")
print(rounds_processed)
