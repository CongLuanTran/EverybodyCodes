use crate::utils::Solution;
use std::fmt::Display;

pub struct Day4;

impl Solution for Day4 {
    const DAY: u32 = 4;

    fn part1(input: &str) -> impl Display {
        let mut gears = input.lines();
        let first: u64 = gears.next().unwrap().parse().unwrap();
        let last: u64 = gears.last().unwrap().parse().unwrap();

        2025 * first / last
    }

    fn part2(input: &str) -> impl Display {
        let mut gears = input.lines();
        let first: f64 = gears.next().unwrap().parse().unwrap();
        let last: f64 = gears.last().unwrap().parse().unwrap();

        (10_000_000_000_000_f64 * last / first).ceil()
    }

    fn part3(input: &str) -> impl Display {
        let mut gears = input.lines().peekable();
        let start: u64 = gears.next().unwrap().parse().unwrap();
        let mut mid: u64 = 1;
        let mut last: u64 = 1;
        while let Some(gear) = gears.next() {
            if gears.peek().is_none() {
                last = gear.parse().unwrap();
                break;
            }
            let (a, b) = gear.split_once("|").unwrap();
            let a: u64 = a.parse().unwrap();
            let b: u64 = b.parse().unwrap();
            mid *= b / a;
        }

        100 * start * mid / last
    }
}
