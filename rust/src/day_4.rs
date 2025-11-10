use crate::utils::{Solution, read_lines, test};
use std::path::PathBuf;

pub struct Day4;

impl Day4 {
    fn get_test(file: PathBuf) -> Vec<String> {
        read_lines(file).unwrap()
    }
}

impl Solution for Day4 {
    fn part1() -> String {
        let gears = Self::get_test(test(4, 1));

        (2025 * gears.first().unwrap().parse::<u64>().unwrap()
            / gears.last().unwrap().parse::<u64>().unwrap())
        .to_string()
    }

    fn part2() -> String {
        let gears = Self::get_test(test(4, 2));

        (10_000_000_000_000_f64 * gears.last().unwrap().parse::<f64>().unwrap()
            / gears.first().unwrap().parse::<f64>().unwrap())
        .ceil()
        .to_string()
    }

    fn part3() -> String {
        let gears = Self::get_test(test(4, 3));
        let start: u64 = gears.first().unwrap().parse().unwrap();
        let end: u64 = gears.last().unwrap().parse().unwrap();
        let teeth = start
            * 100
            * gears[1..gears.len() - 1]
                .iter()
                .map(|l| {
                    let (a, b) = l.split_once("|").unwrap();
                    b.parse::<u64>().unwrap() / a.parse::<u64>().unwrap()
                })
                .product::<u64>();
        (teeth / end).to_string()
    }
}
