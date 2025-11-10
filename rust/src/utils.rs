use std::{
    any::type_name,
    fs, io,
    path::{Path, PathBuf},
};

const BASE_NAME: &str = "everybody_codes_e2025";
const TEST_DIR: &str = "../test/";

pub fn test(day: i8, part: i8) -> PathBuf {
    let filename = format!("{BASE_NAME}_q{day:02}_p{part}.txt");
    Path::new(TEST_DIR).join(filename)
}

pub fn read_text(file: PathBuf) -> io::Result<String> {
    let text = fs::read_to_string(file)?.trim().to_string();
    Ok(text)
}

pub fn read_blocks(file: PathBuf) -> io::Result<Vec<String>> {
    let text = read_text(file)?;
    Ok(text.split("\n\n").map(|s| s.to_string()).collect())
}

pub fn read_lines(file: PathBuf) -> io::Result<Vec<String>> {
    let text = read_text(file)?;
    Ok(text.lines().map(|s| s.to_string()).collect())
}

pub trait Solution {
    fn part1() -> String;
    fn part2() -> String;
    fn part3() -> String;
    fn run() {
        println!("{}:", type_name::<Self>().rsplit("::").next().unwrap());
        println!("\tPart 1: {}", Self::part1());
        println!("\tPart 2: {}", Self::part2());
        println!("\tPart 3: {}", Self::part3());
    }
}
