def _sum(arr):
    sum = 0

    for i in arr:
        sum += i

    return sum


if __name__ == "__main__":
    input_arr = [12, 3, 4, 15]

    print("配列の合計は{}.format(_sum(input_arr))")
