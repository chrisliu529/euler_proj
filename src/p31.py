import time

coins = [200, 100, 50, 20, 10, 5, 2, 1]
count = 0

def collect_ways(n):
    global count
    count = 0
    try_divide(n, 0, 0)
    return count

def try_divide(target, sum, index):
    global count
    for i in range(index, len(coins)):
        coin = coins[i]
        if coin > target:
            continue
        sum_bak = sum
        while sum + coin <= target:
            sum = sum + coin
            if sum == target:
                count = count + 1
            else:
                try_divide(target, sum, i+1)
        sum = sum_bak

def test():
    assert 1 == collect_ways(1)
    assert 2 == collect_ways(2)
    assert 2 == collect_ways(3)
    assert 4 == collect_ways(5)

def solve():
    return collect_ways(200)

if __name__ == "__main__":
    test()
    t = time.time()
    print solve()
    print "(%s)" % (time.time() - t)

