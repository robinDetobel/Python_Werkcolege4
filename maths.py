def fibonacci(n):
    g1, g2 = 0, 1
    count = 0
    getallen = []
    while count < n:
        getallen.append(g1)
        temp = g1 + g2
        g1 = g2
        g2 = temp
        count += 1
    return getallen


def grootste_reeks(*n):
    if n:
        grootste = 0
        for waarde in n:
            if waarde > grootste:
                grootste = waarde
        return grootste



def facrotial (getal):
    counter = 1
    factor = 1
    while counter <= getal:
        factor = factor * counter
        counter += 1
    return factor