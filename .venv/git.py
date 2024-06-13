def hat_allocation(num_cats, num_rounds):
    hats = [False] * num_cats
    for round in range(1, num_rounds + 1):
        for cat in range(round - 1, num_cats, round):
            hats[cat] = not hats[cat]
    return [i + 1 for i, has_hat in enumerate(hats) if has_hat]

num_cats = 100
num_rounds = 100
result = hat_allocation(num_cats, num_rounds)
print(result)



