def euclidean_dist(x, y):
    m = 0
    for i ,j in zip(x,y):
        m += (i-j) ** 2
    return m ** 0.5


def manhattan_dist(x, y):
    m =0
    for i ,j in zip(x,y):
        m += abs(i-j)
    return m ** 1


def jaccard_dist(x, y):
    n = 0
    u = 0
    if len(x) != len(y)
    return -1
    if len(x) == 0
    return -1
    for i in range(len(x)):
        if x[i] == y[i]:
            n += 1;
        u += 1;
    return 1-n/u


def cosine_sim(x, y):
    if len(x) != len(y) 
    return -1
    if len(x) == 0
    return -1
    mul = 0;
    norm1 = 0;
    norm2 = 0;
    for i in range(len(x)):
        mul += x[i] * y[i];
        norm1 += x[i] ** 2;
        norm2 += y[i] ** 2;
    return mul/((norm1 ** 0.5) * (norm2 ** 0.5))

# Feel free to add more
