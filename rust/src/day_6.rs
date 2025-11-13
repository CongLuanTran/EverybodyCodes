use crate::utils::Solution;
use std::fmt::Display;

pub struct Day6;

impl Solution for Day6 {
    const DAY: u32 = 6;
    fn part1(input: &str) -> impl Display {
        let data = input;
        let mut mentors = 0;
        let mut pairs = 0;
        for ch in data.chars() {
            if ch == 'A' {
                mentors += 1;
            } else if ch == 'a' {
                pairs += mentors;
            }
        }

        pairs
    }

    fn part2(input: &str) -> impl Display {
        let data = input;
        let mut mentors = [0, 0, 0];
        let mut pairs = 0;
        for ch in data.bytes() {
            if ch.is_ascii_uppercase() {
                mentors[(ch - b'A') as usize] += 1;
            } else {
                pairs += mentors[(ch.to_ascii_uppercase() - b'A') as usize];
            }
        }

        pairs
    }

    fn part3(input: &str) -> impl Display {
        let rep = 1000;
        let dist = 1000;
        let data = input.as_bytes();
        let size = data.len();
        let mut pairs = 0;

        for (i, ch) in data.iter().enumerate() {
            if ch.is_ascii_lowercase() {
                let mentors = ch.to_ascii_uppercase();

                for j in -dist..dist + 1 {
                    let offset = i as i64 + j;
                    let wrapped = offset.rem_euclid(size as i64) as usize;

                    if data[wrapped] == mentors {
                        pairs += rep - (offset < 0 || offset > size as i64) as u64;
                    }
                }
            }
        }

        pairs
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn part_1() {
        assert_eq!(Day6::part1("ababacacbcbca").to_string(), "5");
    }

    #[test]
    fn part_2() {
        assert_eq!(Day6::part2("ababacacbcbca").to_string(), "3691");
    }

    #[test]
    fn part_3() {
        assert_eq!(
            Day6::part3("aabcbabcabcabcabcabccbaacbca").to_string(),
            "3442321"
        );
    }
}
