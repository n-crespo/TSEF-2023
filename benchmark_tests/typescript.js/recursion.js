//within GitBash terminal, use tsc (filename.ts) to compile, then node (filename.js) to execute
function fib(n) {
    if (n <= 1) {
        return n;
    }
    else {
        return fib(n - 1) + fib(n - 2);
    }
}
for (var i = 0; i < 30; i++) {
    var startTime = new Date().getTime();
    fib(40);
    var endTime = new Date().getTime();
    var duration = endTime - startTime;
    console.log(duration);
}
