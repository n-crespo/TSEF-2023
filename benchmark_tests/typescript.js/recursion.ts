//within GitBash terminal, use tsc (filename.ts) to compile, then node (filename.js) to execute

function fib(n: number): number {
  if (n <= 1) {
    return n;
  } else {
    return fib(n - 1) + fib(n - 2);
  }
}

for (let i = 0; i < 30; i++) {
  const startTime = new Date().getTime();
  fib(40);
  const endTime = new Date().getTime();

  const duration = endTime - startTime;

  console.log(duration);
}
