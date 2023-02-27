#include <iostream>
#include <chrono>
using namespace std;

int fib(int n)
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
  for (int i = 0; i < 30; i++)
  {
    auto start_time = chrono::high_resolution_clock::now();
    long long result = fib(40);
    auto end_time = chrono::high_resolution_clock::now(); 

    auto duration = chrono::duration_cast<chrono::milliseconds>(end_time - start_time).count();

    cout << duration << " ms"<< endl;
  }

  return 0;
}
