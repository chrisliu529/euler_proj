import mtools, time, math

def solve():
    f = open('words.txt')
    s = f.read()
    f.close()
    words = [w[1:len(w)-1] for w in s.split(',')]
    max_len = find_max(words)
    len_words = get_len_words(words, max_len)
    anagram_words = get_anagram_words(len_words)
    anagram_word_len = get_anagram_len(anagram_words)
    words_list = make_words_list(anagram_words)
    square_list = make_square_list()
    #print anagram_words, anagram_max(anagram_words), anagram_word_len
    print words_list
    return max_square(words_list, square_list)

def make_words_list(d):
    l = d.items()
    l2 = [(x, y[0]) for (x, y) in l]
    l2.sort(cmp=lambda x,y: cmp(len(x[0]), len(y[0])), reverse=True)
    return l2

def make_square_list():
    return [str(i*i) for i in range(10000)]

def max_square(wl, sl):
    max = 0
    max_len = 0
    for (src,dist) in wl:
        print src, dist
        if len(src) < max_len:
            return max
        st = [x for x in sl if match_pattern(x, src)]
        for n in st:
            m = replace(src, dist, n)
            #print m, n
            if m in st:
                t = m
                if n > t:
                    t = n
                if t > max:
                    print m,n
                    max = t
                    max_len = len(t)
    return max

def match_pattern(s1, s2):
    if len(s1) != len(s2):
        return False
    mapping = zip(s1, s2)
    mapping.sort()
    for i in range(len(mapping)-1):
        if mapping[i][0] == mapping[i+1][0] and mapping[i][1] != mapping[i+1][1]:
            return False
    return True

def replace(src, dist, n):
    s = ''
    for x in dist:
        s = s + n[src.index(x)]
    return s

def get_anagram_len(d):
    l = []
    for x in d.keys():
        i = len(x)
        if i not in l:
            l.append(i)
    l.sort(reverse=True)
    return l

def anagram_max(d):
    max = 0
    for x in d.values():
        if len(x) > max:
            max = len(x)
    return max

def get_anagram_words(len_words):
    anagram = {}
    for words in len_words:
        for w1 in words:
            l = []
            for w2 in words:
                if w1 == w2:
                    continue
                if same_letters(w1, w2):
                    l.append(w2)
                    words.remove(w2)
            if len(l) > 0:
                anagram[w1] = l
            words.remove(w1)
    return anagram

def same_letters(w1, w2):
    l1 = list(w1)
    l2 = list(w2)
    l1.sort()
    l2.sort()
    return l1 == l2


def get_len_words(words, max_len):
    len_words = []
    for i in range(2, max_len+1):
        tw = [w for w in words if len(w) == i]
        len_words.append(tw)
        words = list(set(words) - set(tw))
    return len_words
 
def find_max(words):
    max = 0
    for w in words:
        if len(w) > max:
            max = len(w)
    return max

def test():
    assert '9216' == replace('CARE', 'RACE', '1296')
    assert '9216' == max_square([('CARE', 'RACE')], make_square_list())

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
