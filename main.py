from typing import List, Tuple


def calculate(usb_size: int, memes: List[Tuple[str, int, int]]) -> Tuple[int, set]:
    """
    Calculates a set of memes which will provide the biggest profit when when sold on a USB stick.

    Params:
    usb_size - the size of the USB stick (int)
    memes - a list of tuples containing the title (str),
    weight in MiB (int) and cost in caps (int) of each meme

    Output:
    (max_cost, res) - a tuple containing the maximum profit which can me acchieved
    as well as the set of meme titles that generate it
    """

    # typechecking the arguments
    if type(usb_size) is not int:
        raise TypeError('usb_size has to be of type int')
    if type(memes) is not list:
        raise TypeError('memes has to be of type list')
    for meme in memes:
        if len(meme) != 3:
            raise ValueError(
                'each element of memes has to be a 3-element tuple')
        n, w, c = meme
        if type(n) is not str:
            raise TypeError(
                'the first argument of a tuple in memes has to be of type string')
        if type(w) is not int:
            raise TypeError(
                'the second argument of a tuple in memes has to be of type int')
        if type(c) is not int:
            raise TypeError(
                'the third argument of a tuple in memes has to be of type int')

    # preproccesing the arguments
    num_of_memes = len(memes)
    size = usb_size*1024
    weights = [0] + [meme[1] for meme in memes]
    costs = [0] + [meme[2] for meme in memes]
    memo_tab = [[0] * (size + 1) for _ in range(num_of_memes + 1)]
    res = set()

    # filling up the memoization table to get the maximum cost
    for i in range(num_of_memes + 1):
        for j in range(size + 1):
            if i == 0 or j == 0:
                memo_tab[i][j] = 0
            elif weights[i] <= j:
                memo_tab[i][j] = max(
                    costs[i] + memo_tab[i - 1][j-weights[i]], memo_tab[i - 1][j])
            else:
                memo_tab[i][j] = memo_tab[i - 1][j]
    max_cost = memo_tab[-1][j]

    # backtracking to retrieve the meme titles, which provide the highest profit
    n, m = num_of_memes, size
    while n > 0 and m > 0:
        if memo_tab[n][m] == memo_tab[n - 1][m]:
            n -= 1
        else:
            res.add(memes[n - 1][0])
            m = m - weights[n]
            n -= 1

    return (max_cost, res)
