#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

// Recursive function to calculate the nth term of the Fibonacci sequence
long long fib(int n)
{
  if (n <= 1)
  {
    return n;
  }
  else
  {
    return fib(n - 1) + fib(n - 2);
  }
}

int main()
{
  // Call fib(40) 30 times and time each call
  for (int i = 0; i < 30; i++)
  {
    struct timeval start_time, end_time;
    gettimeofday(&start_time, NULL); // get start time
    fib(40);
    gettimeofday(&end_time, NULL); // get end time

    // Calculate the duration in milliseconds
    long long duration = (end_time.tv_sec - start_time.tv_sec) * 1000 + (end_time.tv_usec - start_time.tv_usec) / 1000;

    printf("%lld\n", duration);
  }

  return 0;
}
