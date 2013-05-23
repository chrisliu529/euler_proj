#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>

#define _dim(s) (sizeof(s)/sizeof(*s))

long find_greatest_clip(long *arr, int size)
{
    long s = 0, e = 0;
    int i;
    for (i = 0; i < size; i++) {
        s += arr[i];
        if (s < 0) {
            s = 0;
        }
        if (e < s) {
            e = s;
        }
    }
    return e;
}

long find_greatest(long *tab, int rows)
{
    int n = rows*rows;
    long max = LONG_MIN;
    long s = 0;
    int i, j = 0;
    int si;
    int cnt;
    long v;
    int t;
    long *arr = (long *)malloc(2*rows*sizeof(long));

    //check horizontal
    printf("************Horizontal*************\n");
    t = 1;
    while (j < n) {
        printf("%d:",t);
        for (i = 0; i < rows; i ++) {
            v = tab[j+i];
            arr[i] = v;
        }
        t++;
        printf("\n");
        s = find_greatest_clip(arr, rows);
        if (s > max) {
            max = s;
            printf("new max=%ld\n", max);
        }
        j += rows;
    }

    //check vertical
    printf("************Vertical*************\n");
    t = 1;
    for (i = 0; i < rows; i ++) {
        printf("%d:",t);
        for (j = 0; j < rows; j ++) {
            v = tab[i+j*rows];
            arr[j] = v;
        }
        t++;
        printf("\n");
        s = find_greatest_clip(arr, rows);
        if (s > max) {
            max = s;
            printf("new max=%ld\n", max);
        }
    }

    //check diag
    //locate starting elem
    printf("************Diagonal*************\n");
    t = 1;
    for (i = 0; i < rows; i ++) {
        si = rows*(rows-i);
        cnt = 0;
        printf("%d:",t);
        while (si < n) {
            v = tab[si];
            arr[cnt++] = v;
            si += (rows+1);
        }
        t++;
        printf("\n");
        s = find_greatest_clip(arr, cnt);
        if (s > max) {
            max = s;
            printf("new max=%ld\n", max);
        }
    }
    for (i = 1; i < rows; i ++) {
        j = rows-i;
        si = i;
        cnt = 0;
        printf("%d:",t);
        while (cnt < j) {
            v = tab[si];
            arr[cnt++] = v;
            si += (rows+1);
        }
        t++;
        printf("\n");
        s = find_greatest_clip(arr, cnt);
        if (s > max) {
            max = s;
            printf("new max=%ld\n", max);
        }
    }

    //check anti-diag
    printf("************Anti-Diagonal*************\n");
    t = 1;
    for (i = 0; i < rows; i ++) {
        si = i*rows;
        j = i+1;
        cnt = 0;
        printf("%d:",t);
        while (cnt < j) {
            v = tab[si];
            arr[cnt++] = v;
            si -= (rows-1);
        }
        t++;
        printf("\n");
        s = find_greatest_clip(arr, cnt);
        if (s > max) {
            max = s;
            printf("new max=%ld\n", max);
        }
    }
    for (i = n-rows+1; i < n; i ++) {
        cnt = 0;
        j = n-i;
        si = i;
        printf("%d:",t);
        while (cnt < j) {
            v = tab[si];
            arr[cnt++] = v;
            si -= (rows-1);
        }
        t++;
        printf("\n");
        s = find_greatest_clip(arr, cnt);
        if (s > max) {
            max = s;
            printf("new max=%ld\n", max);
        }
    }

    return max;
}

void test_find_greatest()
{
    long arr[] = {-2, 5, 3, 2, 9, -6, 5, 1, 3, 2, 7, 3, -1, 8, -4, 8};
    assert(16 == find_greatest(arr, 4));

    long arr2[] = {1, 2, -6, 3, -2, 4, -1, 3, 2, -4};
    assert(9 == find_greatest_clip(arr2, _dim(arr2)));
}

long *build_tab(n)
{
    int sz = n*n;
    long *s = (long *)malloc(sz*sizeof(long));
    long i, k;
    /*For 1<=k<=55, s[k] = [100003 - 200003k + 300007*k^3] (modulo 1000000) - 500000.
     *For 56<=k<=4000000, s[k] = [s[k-24] + s[k-55] + 1000000] (modulo 1000000) - 500000.
     */
    for (k = 1; k <= 55; k ++) {
        long v = (100003 - 200003*k + 300007*k*k*k)%1000000 - 500000;
        s[k-1] = v;
    }
    for (k = 56; k <= sz; k ++) {
        i = k-1;
        s[i] = (s[i-24] + s[i-55] + 1000000)%1000000 - 500000;
    }

    assert((-393027 == s[9]) && (86613 == s[99]));
    return s;
}

int main()
{
    test_find_greatest();
    long *tab = build_tab(2000);
    long max = find_greatest(tab, 2000);
    printf("max=%ld\n", max);
    return 0;
}

