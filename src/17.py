digit_string = ["","one","two","three","four","five","six","seven","eight","nine"]
tab = [len(x) for x in digit_string]

teen_string = ["ten","eleven","twelve","thirteen","fourteen","fifteen",
               "sixteen","seventeen","eighteen","nineteen"]
teen_tab = [len(x) for x in teen_string]

ty_string = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
ty_tab = [len(x) for x in ty_string]

def two_digit_letters_number(n):
    global tab,teen_tab,ty_tab
    if n < 10:
        return tab[n]
    elif n < 20:
        return teen_tab[n-10]
    else:
        r = n - 20
        return ty_tab[r/10] + tab[r%10]

def letters_number(n):
    global tab
    assert n >= 1 and n <= 1000
    if (n == 1000):
        return 11
    h = n/100
    t = n-100*h
    sum = tab[h] + two_digit_letters_number(t)
    if (h > 0):
        sum += 7 #len("hundred")
        if (t > 0):
            sum += 3 #len("and")
    return sum

def sum_letters_number(n):
    l = [letters_number(x) for x in range(1, n+1)]
    return sum(l)

def test_letters_number():
    l = [(1000,11),(342,23),(115,20),(11,6),(12,6),(100,10)]
    for (input,output) in l:
        assert letters_number(input) == output

def test():
    test_letters_number()

def main():
    print sum_letters_number(1000)

if __name__ == "__main__":
    test()
    main()
