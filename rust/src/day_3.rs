use std::collections::{BTreeSet, HashMap, HashSet};

use crate::utils::{Solution, read_text, test};

pub struct Day3;

impl Solution for Day3 {
    type Output = Vec<i32>;

    fn get_test(file: std::path::PathBuf) -> Self::Output {
        read_text(file)
            .unwrap()
            .split(",")
            .map(|s| s.parse::<i32>().unwrap())
            .collect()
    }

    fn part1() -> String {
        let nums = Self::get_test(test(3, 1));
        nums.iter()
            .collect::<HashSet<_>>()
            .iter()
            .copied()
            .sum::<i32>()
            .to_string()
    }

    fn part2() -> String {
        let nums = Self::get_test(test(3, 2));
        nums.iter()
            .collect::<BTreeSet<_>>()
            .iter()
            .take(20)
            .copied()
            .sum::<i32>()
            .to_string()
    }

    fn part3() -> String {
        let nums = Self::get_test(test(3, 3));
        nums.iter()
            .fold(HashMap::new(), |mut acc, &num| {
                *acc.entry(num).or_insert(0) += 1;
                acc
            })
            .values()
            .copied()
            .max()
            .unwrap()
            .to_string()
    }
}
