import pandas as pd


def findS():
    dataarr = pd.read_csv("ENJOYSPORT.csv", header=None)
    dataarr = dataarr.values.tolist()
    print(len(dataarr))
    h = ["0", "0", "0", "0", "0", "0"]
    rows = len(dataarr)
    columns = 7
    for x in range(1, rows):
        t = dataarr[x]
        print(t)
        if t[columns - 1] == "1":
            for y in range(0, columns - 1):
                if h[y] == t[y]:
                    pass
                elif h[y] != t[y] and h[y] == "0":
                    h[y] = t[y]
                elif h[y] != t[y] and h[y] != "0":
                    h[y] = "?"
        print(h)

    print("Maximally Specific set")
    print("<", end=" ")
    print(*h, sep=", ", end=", >")


findS()
