rows1 = int(input("Enter rows for first matrix: "))
cols1 = int(input("Enter columns for first matrix: "))
rows2 = int(input("Enter rows for second matrix: "))
cols2 = int(input("Enter columns for second matrix: "))

if cols1 != rows2:
    print("Matrix multiplication is not possible.")
else:
    first = []
    second = []

    print("Enter first matrix values:")
    for i in range(rows1):
        row = list(map(int, input().split()))
        first.append(row)

    print("Enter second matrix values:")
    for i in range(rows2):
        row = list(map(int, input().split()))
        second.append(row)

    product = []
    for i in range(rows1):
        result_row = []
        for j in range(cols2):
            total = 0
            for k in range(cols1):
                total = total + first[i][k] * second[k][j]
            result_row.append(total)
        product.append(result_row)

    print("Product matrix:")
    for row in product:
        print(*row)
