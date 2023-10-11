def chocolates_with_money(m, c):
    chocolates_bought = m // c
    wrappers = chocolates_bought
    total_chocolates = chocolates_bought

    while wrappers >= 3:
        additional_chocolates = wrappers // 3
        total_chocolates += additional_chocolates
        wrappers = additional_chocolates + (wrappers % 3)

    return total_chocolates


# Example usage:
# m = 15  # Amount in Rupees
# c = 2  # Cost of one chocolate in Rupees
print("enter comma separated value for m and c")
input_str = input()
m = input_str.split(",")
result = chocolates_with_money(int(m[0]), int(m[1]))
print(f"You can get {result} chocolates.")
