use crate::utils::Solution;
use std::collections::{BTreeSet, HashMap, HashSet};
use std::fmt::Display;

pub struct Day3;

impl Solution for Day3 {
    const DAY: u32 = 3;

    fn part1(input: &str) -> impl Display {
        input
            .split(",")
            .map(|s| s.parse::<i32>().unwrap())
            .collect::<HashSet<_>>()
            .iter()
            .copied()
            .sum::<i32>()
    }

    fn part2(input: &str) -> impl Display {
        input
            .split(",")
            .map(|s| s.parse::<i32>().unwrap())
            .collect::<BTreeSet<_>>()
            .iter()
            .take(20)
            .copied()
            .sum::<i32>()
    }

    fn part3(input: &str) -> impl Display {
        input
            .split(",")
            .map(|s| s.parse::<i32>().unwrap())
            .fold(HashMap::new(), |mut acc, num| {
                *acc.entry(num).or_insert(0) += 1;
                acc
            })
            .values()
            .copied()
            .max()
            .unwrap()
    }
}
