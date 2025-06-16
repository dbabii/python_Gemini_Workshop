def compute_usd_total(ammount_in_aud=0, amount_in_gbp=0):
    total = 0
    total += ammount_in_aud * 0.78
    total += amount_in_gbp * 1.29
    return total

print(compute_usd_total(amount_in_gbp=10))