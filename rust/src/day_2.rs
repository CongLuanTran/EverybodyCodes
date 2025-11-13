use crate::utils::Solution;
use num_complex::Complex;
use rayon::iter::{IntoParallelIterator, ParallelIterator};
use std::fmt::Display;

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

impl Solution for Day2 {
    const DAY: u32 = 2;

    fn part1(input: &str) -> impl Display {
        let (x, y) = input.trim()[3..input.len() - 1].split_once(",").unwrap();
        let x: i32 = x.parse().unwrap();
        let y: i32 = y.parse().unwrap();
        let a = Complex::new(x, y);
        let mut r = Complex::new(0, 0);
        let div = 10;
        for _ in 0..3 {
            r *= r;
            r /= div;
            r += a;
        }

        format!("[{},{}]", r.re, r.im)
    }

    fn part2(input: &str) -> impl Display {
        let (x, y) = input.trim()[3..input.len() - 1].split_once(",").unwrap();
        let x: i64 = x.parse().unwrap();
        let y: i64 = y.parse().unwrap();

        let mut count: u64 = 0;
        for i in 0..101 {
            for j in 0..101 {
                if check(Complex::new(x + 10 * i, y + 10 * j)) {
                    count += 1;
                }
            }
        }

        count
    }

    fn part3(input: &str) -> impl Display {
        let (x, y) = input.trim()[3..input.len() - 1].split_once(",").unwrap();
        let x: i64 = x.parse().unwrap();
        let y: i64 = y.parse().unwrap();

        (0..1001)
            .into_par_iter()
            .map(|i| {
                let mut count: u64 = 0;

                for j in 0..1001 {
                    if check(Complex::new(x + i, y + j)) {
                        count += 1;
                    }
                }
                count
            })
            .sum::<u64>()
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn part_1() {
        assert_eq!(Day2::part1("A=[25,9]").to_string(), "[357,862]");
    }

    #[test]
    fn part_2() {
        assert_eq!(Day2::part2("A=[35300,-64910]").to_string(), "4076");
    }

    #[test]
    fn part_3() {
        assert_eq!(Day2::part3("A=[35300,-64910]").to_string(), "406954");
    }
}
