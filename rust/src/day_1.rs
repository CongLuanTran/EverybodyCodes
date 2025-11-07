use std::{
    cmp::{max, min},
    path::PathBuf,
};

use crate::utils::{read_blocks, test};

fn get_test(file: PathBuf) -> (Vec<String>, Vec<String>) {
    let [names, moves] = read_blocks(file).unwrap().try_into().unwrap();
    (
        names.split(",").map(|s| s.trim().to_string()).collect(),
        moves.split(",").map(|s| s.trim().to_string()).collect(),
    )
}

fn part1() {
    let (names, moves) = get_test(test(1, 1));
    let length = names.len() as i32 - 1;
    let index = moves.iter().fold(0, |acc, expr| {
        if expr.starts_with("R") {
            let val: i32 = expr.strip_prefix("R").unwrap().parse().unwrap();
            min(acc + val, length)
        } else {
            let val: i32 = expr.strip_prefix("L").unwrap().parse().unwrap();
            max(acc - val, 0)
        }
    });

    println!("\tPart 1: {}", names[index as usize]);
}

fn part2() {
    let (names, moves) = get_test(test(1, 2));
    let length = names.len() as i32;
    let index = moves.iter().fold(0, |acc, expr| {
        let val = if expr.starts_with("R") {
            expr.strip_prefix("R").unwrap().parse().unwrap()
        } else {
            -expr.strip_prefix("L").unwrap().parse::<i32>().unwrap()
        };
        (acc + val + length) % length
    });

    println!("\tPart 2: {}", names[index as usize]);
}

fn part3() {
    let (mut names, moves) = get_test(test(1, 3));
    let length = names.len();
    for m in moves {
        let i: usize = if m.starts_with("R") {
            m.strip_prefix("R").unwrap().parse::<usize>().unwrap() % length
        } else {
            length - m.strip_prefix("L").unwrap().parse::<usize>().unwrap() % length
        };
        names.swap(0, i);
    }

    println!("\tPart 3: {}", names[0]);
}

pub fn day1() {
    println!("Day 1:");
    part1();
    part2();
    part3();
}
