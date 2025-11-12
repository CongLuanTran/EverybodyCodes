use crate::utils::{Solution, read_text, test};
use std::{collections::HashMap, path::PathBuf};

pub struct Day6;

fn get_test(file: PathBuf) -> String {
    read_text(file).unwrap()
}

impl Solution for Day6 {
    fn part1() -> String {
        let data = get_test(test(6, 1));
        let mut knight: HashMap<char, Vec<u32>> = HashMap::new();
        let mut novice: HashMap<char, Vec<u32>> = HashMap::new();
        for (i, ch) in data.char_indices() {
            if ch.is_lowercase() {
                novice.entry(ch).or_default().push(i as u32);
            } else {
                knight.entry(ch).or_default().push(i as u32);
            }
        }
        let lower = novice.get(&'a').unwrap();
        let upper = knight.get(&'A').unwrap();
        let sum = lower.iter().fold(0u32, |a, b| {
            a + upper.binary_search(b).err().unwrap() as u32
        });

        sum.to_string()
    }

    fn part2() -> String {
        let data = get_test(test(6, 2));
        let mut knight: HashMap<char, Vec<u32>> = HashMap::new();
        let mut novice: HashMap<char, Vec<u32>> = HashMap::new();
        for (i, ch) in data.char_indices() {
            if ch.is_lowercase() {
                novice.entry(ch).or_default().push(i as u32);
            } else {
                knight.entry(ch).or_default().push(i as u32);
            }
        }
        let sum = "abc".chars().fold(0u32, |a, b| {
            let lower = novice.get(&b).unwrap();
            let upper = knight.get(&b.to_ascii_uppercase()).unwrap();

            let b = lower.iter().fold(0u32, |a, b| {
                a + upper.binary_search(b).unwrap_or_else(|i| i) as u32
            });
            a + b
        });

        sum.to_string()
    }

    fn part3() -> String {
        let rep = 1000;
        let dist = 1000;
        let data = get_test(test(6, 3)).repeat(rep);
        let mut knight: HashMap<char, Vec<u64>> = HashMap::new();
        let mut novice: HashMap<char, Vec<u64>> = HashMap::new();
        for (i, ch) in data.char_indices() {
            if ch.is_lowercase() {
                novice.entry(ch).or_default().push(i as u64);
            } else {
                knight.entry(ch).or_default().push(i as u64);
            }
        }
        let sum = "abc".chars().fold(0u64, |a, b| {
            let lower = novice.get(&b).unwrap();
            let upper = knight.get(&b.to_ascii_uppercase()).unwrap();

            let b = lower.iter().fold(0u64, |a, b| {
                let left = b.saturating_sub(dist);
                let right = (b + dist).min(data.len() as u64);
                let left_idx = upper.partition_point(|&x| x < left);
                let right_idx = upper.partition_point(|&x| x <= right); // exclusive upper
                a + (right_idx - left_idx) as u64
            });
            a + b
        });

        sum.to_string()
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn day_6_part_1() {
        assert_eq!(Day6::part1(), "162");
    }

    #[test]
    fn day_6_part_2() {
        assert_eq!(Day6::part2(), "3691");
    }

    #[test]
    fn day_6_part_3() {
        assert_eq!(Day6::part3(), "1667255418");
    }
}
