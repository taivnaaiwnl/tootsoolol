import os


def dp_make_weight_with_details(egg_weights, target_weight):
    memo = [0] * (target_weight + 1)
    choices = [[] for _ in range(target_weight + 1)]

    def dp(egg_weights, target_weight, memo, choices):
        if target_weight in egg_weights:
            memo[target_weight] = 1
            choices[target_weight] = [target_weight]
            return 1, [target_weight]
        elif memo[target_weight] > 0:
            return memo[target_weight], choices[target_weight]
        else:
            minEggs = float("inf")
            best_choice = []
            for i in [c for c in egg_weights if c <= target_weight]:
                numEggs, choice = dp(egg_weights, target_weight - i, memo, choices)
                numEggs += 1
                if numEggs < minEggs:
                    minEggs = numEggs
                    best_choice = choice + [i]
            memo[target_weight] = minEggs
            choices[target_weight] = best_choice
            return minEggs, best_choice

    num_eggs, choice_list = dp(egg_weights, target_weight, memo, choices)
    choice_counts = {egg: choice_list.count(egg) for egg in set(choice_list)}
    return num_eggs, choice_counts


if __name__ == "__main__":
    egg_weights = (1, 5, 10, 25)
    n = 100
    num_eggs, choice_counts = dp_make_weight_with_details(egg_weights, n)

    choices_str = " + ".join(
        [f"{count} * {weight}" for weight, count in choice_counts.items()]
    )
    actual_output = f"{num_eggs} ({choices_str} = 99)"

    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = {n})")
    print(f"Actual output: {actual_output}")
