use crate::utils::Solution;
use std::fmt::Display;

pub struct Day8;

impl Solution for Day8 {
    const DAY: u32 = 8;

    fn part1(note: &str) -> impl Display {
        let nails = get_nail(note);
        let half = 16;
        nails
            .windows(2)
            .filter(|p| p[0].abs_diff(p[1]) == half as u32)
            .count()
    }

    fn part2(note: &str) -> impl Display {
        let nails = get_nail(note);
        let pairs: Vec<(u32, u32)> = nails
            .windows(2)
            .map(|p| (p[0].min(p[1]), p[0].max(p[1])))
            .collect();
        let mut knot = 0u64;
        for (i, (a, b)) in pairs.iter().enumerate().skip(1) {
            for (c, d) in pairs.iter().take(i) {
                if (a > c && d > a && b > d) || (a < c && c < b && b < d) {
                    knot += 1;
                }
            }
        }
        knot
    }

    fn part3(note: &str) -> impl Display {
        let nails = get_nail(note);
        let pairs: Vec<(u32, u32)> = nails
            .windows(2)
            .map(|p| (p[0].min(p[1]), p[0].max(p[1])))
            .collect();
        let mut best = 1u64;
        for (a, b) in pairs.iter() {
            let mut knot = 1u64;
            for (c, d) in pairs.iter() {
                if (a > c && d > a && b > d) || (a < c && c < b && b < d) || (a == c && b == d) {
                    knot += 1;
                }
            }
            best = best.max(knot);
        }
        best
    }
}

fn get_nail(note: &str) -> Vec<u32> {
    note.split(",").map(|s| s.parse().unwrap()).collect()
}

#[cfg(test)]
mod test {
    use super::*;
    use crate::utils::test;

    #[test]
    fn part_1_real() {
        assert_eq!(Day8::part1(&test(8, 1)).to_string(), "54")
    }

    #[test]
    fn part_2() {
        let test = "1,5,2,6,8,4,1,7,3,5,7,8,2";
        assert_eq!(Day8::part2(test).to_string(), "21")
    }

    #[test]
    fn part_2_real() {
        assert_eq!(Day8::part2(&test(8, 2)).to_string(), "2921491")
    }

    #[test]
    fn part_3() {
        let test = "1,5,2,6,8,4,1,7,3,6";
        assert_eq!(Day8::part3(test).to_string(), "7")
    }

    #[test]
    fn part_3_real() {
        assert_eq!(Day8::part3(&test(8, 3)).to_string(), "7")
    }
}
