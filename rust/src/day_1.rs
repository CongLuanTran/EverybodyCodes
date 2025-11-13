use crate::utils::Solution;
use std::cmp::{max, min};
use std::fmt::Display;

pub struct Day1;

impl Solution for Day1 {
    const DAY: u32 = 1;
    fn part1(input: &str) -> impl Display {
        let (names, moves) = input.split_once("\n\n").unwrap();
        let names = names.split(",").collect::<Vec<&str>>();
        let moves = moves.split(",");
        let length = names.len() - 1usize;
        let index = moves.fold(0, |acc, expr| {
            if expr.starts_with("R") {
                let val: i32 = expr.strip_prefix("R").unwrap().parse().unwrap();
                min(acc + val, length as i32)
            } else {
                let val: i32 = expr.strip_prefix("L").unwrap().parse().unwrap();
                max(acc - val, 0)
            }
        });

        names[index as usize]
    }

    fn part2(input: &str) -> impl Display {
        let (names, moves) = input.split_once("\n\n").unwrap();
        let names = names.split(",").collect::<Vec<&str>>();
        let moves = moves.split(",");
        let length = names.len() as i32;
        let index = moves.fold(0, |acc, expr| {
            let val = if expr.starts_with("R") {
                expr.strip_prefix("R").unwrap().parse().unwrap()
            } else {
                -expr.strip_prefix("L").unwrap().parse::<i32>().unwrap()
            };
            (acc + val + length) % length
        });

        names[index as usize]
    }

    fn part3(input: &str) -> impl Display {
        let (names, moves) = input.split_once("\n\n").unwrap();
        let mut names = names.split(",").collect::<Vec<&str>>();
        let moves = moves.split(",");
        let length = names.len();
        for m in moves {
            let i: usize = if m.starts_with("R") {
                m.strip_prefix("R").unwrap().parse::<usize>().unwrap() % length
            } else {
                length - m.strip_prefix("L").unwrap().parse::<usize>().unwrap() % length
            };
            names.swap(0, i);
        }

        names[0]
    }
}
