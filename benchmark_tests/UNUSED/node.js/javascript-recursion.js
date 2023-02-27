function fibonacci(n) {
    if (n == 0){
        return 0;
    }else if (n == 1){
        return 1
    }else{
        return fibonacci(n-1) + fibonacci(n-2);
    }
}
x = 0
while (x < 30){
    console.time('test');
    fibonacci(40);
    console.timeEnd('test');
    x += 1}