//use 'dotnet run'
using System;

namespace Fibonacci
{
    class Program
    {
        // Recursive function to calculate the nth term of the Fibonacci sequence
        static long Fib(int n)
        {
            if (n <= 1)
            {
                return n;
            }
            else
            {
                return Fib(n - 1) + Fib(n - 2);
            }
        }

        static void Main(string[] args)
        {
            // Call Fib(40) 30 times and time each call
            for (int i = 0; i < 30; i++)
            {
                DateTime startTime = DateTime.Now;
                long result = Fib(40);
                DateTime endTime = DateTime.Now;

                // Calculate the duration in milliseconds
                long duration = (long)endTime.Subtract(startTime).TotalMilliseconds;

                Console.WriteLine("Call took {0} milliseconds.", duration);
            }
        }
    }
}
