#include <stdio.h>
#include <assert.h>

unsigned int powers[32];

void init()
{
    int i;
    unsigned int p = 1;
    for (i = 0; i < 32; i ++) {
        powers[i] = (p << i);
    }
}

int X(unsigned int a, unsigned int b, unsigned int c)
{
    int i, s, ta, tb, tc;
    for (i = 0; i < 32; i ++) {
        unsigned p = powers[i];
        if (p > c) break;
        ta = (a & p) >> i;
        tb = (b & p) >> i;
        tc = (c & p) >> i;
        s = ta + tb + tc;
        if (s & 1) return 1;
    }
    return 0;
}

void test()
{
    assert(0 == X(1,2,3));
    assert(X(3,5,7));
}

unsigned int solve()
{
    unsigned int n;
    unsigned int res = 0;
    unsigned int nm = 1<<30;

    for (n = 1; n <= nm; n ++) {
        if (0 == X(n, 2*n, 3*n)) res ++;
    }
    return res;
}

int main()
{
    init();
    test();
    printf("answer=%u\n", solve());
    return 0;
}

