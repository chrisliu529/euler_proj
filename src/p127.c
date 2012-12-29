/*adapted from code in page http://www.mathblog.dk/files/euler/Problem127.cs*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <time.h>

#ifdef __MACH__
#include <mach/clock.h>
#include <mach/mach.h>
#endif

void current_utc_time(struct timespec *ts) {

#ifdef __MACH__ // OS X does not have clock_gettime, use clock_get_time
  clock_serv_t cclock;
  mach_timespec_t mts;
  host_get_clock_service(mach_host_self(), CALENDAR_CLOCK, &cclock);
  clock_get_time(cclock, &mts);
  mach_port_deallocate(mach_task_self(), cclock);
  ts->tv_sec = mts.tv_sec;
  ts->tv_nsec = mts.tv_nsec;
#else
  clock_gettime(CLOCK_REALTIME, ts);
#endif

}

long to_ms(struct timespec *t)
{
  return t->tv_sec*1000 + t->tv_nsec/1000000;
}

long ms_diff(struct timespec *t_start, struct timespec *t_end)
{
  return to_ms(t_end) - to_ms(t_start);
}

long GCD(long a, long b) {
  return b == 0 ? a : GCD(b, a % b);
}

int Bruteforce(long limit) {
  long long result = 0;
            
  //Sieve all radicals
  long *radicals = (long *)malloc(limit*sizeof(long));
  long i, j;
  for (i = 0; i < limit; i++) {
    radicals[i] = 1;
  }

  for (i = 2; i < limit; i++) {
    if (radicals[i] == 1) {
      radicals[i] = i;

      for (j = i + i; j < limit; j += i) {
	radicals[j] *= i;
      }
    }
  }
     
  long lim2 = (long)(limit/2.0+0.5);
  long a,b;
  //Check for the properties
  for (a = 1; a < lim2; a++) {
    for (b = a + 1; b < limit-a; b++) {
      long c = a+b;
      if ((radicals[a] * radicals[b] * radicals[c] <c) && (GCD(a, b) == 1))
	result += a + b;
    }
  }

  return result;
}

int main()
{
  struct timespec start, end;
  current_utc_time(&start);
  long long res = Bruteforce(120000);
  current_utc_time(&end);
  printf("%lld (%ld)\n", res, ms_diff(&start, &end));
  return 0;
}
