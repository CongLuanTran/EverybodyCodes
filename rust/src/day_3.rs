use crate::utils::{Solution, read_text, test};
use std::{
    collections::{BTreeSet, HashMap, HashSet},
    path::PathBuf,
};

pub struct Day3;

impl Day3 {
    fn get_test(file: PathBuf) -> Vec<i32> {
        read_text(file)
            .unwrap()
            .split(",")
            .map(|s| s.parse::<i32>().unwrap())
            .collect()
    }
}

impl Solution for Day3 {
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
