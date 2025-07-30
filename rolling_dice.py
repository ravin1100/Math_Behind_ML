import random

# Counters for sums
count_7 = 0
count_2 = 0
count_gt_10 = 0

for _ in range(10000):
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)

    total = num1 + num2

    if total == 7:
        count_7 += 1
    elif total == 2:
        count_2 += 1
    elif total > 10:
        count_gt_10 += 1


# Calculate estimated probabilities
prob_7 = count_7 / 10000
prob_2 = count_2 / 10000
prob_gt_10 = count_gt_10 / 10000


print(f"Estimated Probability of sum = 7: {prob_7}")
print(f"Estimated Probability of sum = 2: {prob_2}")
print(f"Estimated Probability of sum > 10: {prob_gt_10}")

