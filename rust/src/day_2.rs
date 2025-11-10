use crate::utils::{Solution, read_text, test};
use num_complex::Complex;
use rayon::iter::{IntoParallelIterator, ParallelIterator};
use std::path::PathBuf;

fn check(x: Complex<i64>) -> bool {
    let mut r = Complex::new(0, 0);
    let div = 100000;
    for _ in 0..100 {
        r *= r;
        r /= div;
        r += x;
        if r.re.abs() > 1000000 || r.im.abs() > 1000000 {
            return false;
        }
    }
    true
}

pub struct Day2;

impl Day2 {
    fn get_test(file: PathBuf) -> (i64, i64) {
        let s = read_text(file).unwrap();
        let mut it = s[3..s.len() - 1]
            .split(",")
            .map(|c| c.parse::<i64>().unwrap());
        (it.next().unwrap(), it.next().unwrap())
    }
}

impl Solution for Day2 {
    fn part1() -> String {
        let (x, y) = Self::get_test(test(2, 1));
        let a = Complex::new(x, y);
        let mut r = Complex::new(0, 0);
        let div = 10;
        for _ in 0..3 {
            r *= r;
            r /= div;
            r += a;
        }

        format!("[{}, {}]", r.re, r.im)
    }

    fn part2() -> String {
        let (x, y) = Self::get_test(test(2, 2));

        let mut count = 0;
        for i in 0..101 {
            for j in 0..101 {
                if check(Complex::new(x + 10 * i, y + 10 * j)) {
                    count += 1;
                }
            }
        }

        count.to_string()
    }

    fn part3() -> String {
        let (x, y) = Self::get_test(test(2, 2));

        (0..1001)
            .into_par_iter()
            .map(|i| {
                let mut count = 0;

                for j in 0..1001 {
                    if check(Complex::new(x + i, y + j)) {
                        count += 1;
                    }
                }
                count
            })
            .sum::<u32>()
            .to_string()
    }
}
