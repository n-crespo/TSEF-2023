fn fib(n: i32) -> i32 {
    if n <= 1 {
        return n;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}

fn main() {
    for _i in 0..30 {
        let start = std::time::Instant::now();
        fib(40);
        let end = std::time::Instant::now();
        println!("{}ms", end.duration_since(start).as_millis());
    }
}
