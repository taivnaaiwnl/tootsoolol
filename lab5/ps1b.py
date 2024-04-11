def dp_make_weight(egg_weights, target_weight, memo):
    minEggs = target_weight
    if target_weight in egg_weights:
        memo[target_weight] = 1
        return 1
    elif memo[target_weight] > 0:
        return memo[target_weight]
    else:
        for i in [c for c in egg_weights if c <= target_weight]:
            numEggs = 1 + dp_make_weight(egg_weights, target_weight - i, memo)
            if numEggs < minEggs:
                minEggs = numEggs
                memo[target_weight] = minEggs
    return minEggs


if __name__ == "__main__":
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n, memo=[0] * (n + 1)))
    print()
