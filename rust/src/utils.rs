use std::{fmt::Display, fs, path::Path};

const BASE_NAME: &str = "everybody_codes_e2025";
const TEST_DIR: &str = "../test/";

pub fn test(day: u32, part: u32) -> String {
    let filename = format!("{BASE_NAME}_q{day:02}_p{part}.txt");
    let path = Path::new(TEST_DIR).join(filename);
    fs::read_to_string(path).unwrap()
}

pub trait Solution {
    const DAY: u32;
    fn part1(note: &str) -> impl Display;
    fn part2(note: &str) -> impl Display;
    fn part3(note: &str) -> impl Display;
    fn run() {
        println!("Day {}", Self::DAY);
        println!("\tPart 1: {}", Self::part1(&test(Self::DAY, 1)));
        println!("\tPart 2: {}", Self::part2(&test(Self::DAY, 2)));
        println!("\tPart 3: {}", Self::part3(&test(Self::DAY, 3)));
    }
}
