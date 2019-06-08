usb_size = 1
memes = [
    ('rollsafe.jpg', 205, 6),
    ('sad_pepe_compilation.gif', 410, 10),
    ('yodeling_kid.avi', 605, 12)
]

usb_size2 = 64
memes2 = [
    ('a', 204, 70,),
    ('b', 22400, 800),
    ('c', 234, 80),
    ('d', 5000, 240),
    ('e', 64000, 6700),
    ('f', 32000, 5400),
    ('g', 32000, 5300)
]


def calculate(usb_size, memes):
    num_of_memes = len(memes)
    size = usb_size*1024
    weights = [0] + [memes[i][1] for i in range(num_of_memes)]
    costs = [0] + [memes[i][2] for i in range(num_of_memes)]
    tab = [[0 for cols in range(size+1)] for rows in range(num_of_memes+1)]
    res = set({})
    for i in range(0, num_of_memes+1):
        for j in range(0, size+1):
            if i == 0 or j == 0:
                tab[i][j] = 0
            elif weights[i] <= j:
                tab[i][j] = max(costs[i] + tab[i-1][j-weights[i]], tab[i-1][j])
            else:
                tab[i][j] = tab[i-1][j]
    cost = tab[num_of_memes][j]
    n, m = num_of_memes, size
    while n > 0 and m > 0:
        if tab[n][m] == tab[n-1][m]:
            n -= 1
        else:
            res.add(memes[n-1][0])
            m = m - weights[n]
            n -= 1
    return (cost, res)


print(calculate(usb_size, memes))
print(calculate(usb_size2, memes2))
