use crate::utils::Solution;
use std::{
    collections::{HashMap, HashSet, VecDeque},
    fmt::Display,
};

fn valid_name(name: &str, rules: &HashMap<u8, Vec<u8>>) -> bool {
    let chars = name.bytes();
    let mut curr_ch = b'^';
    for ch in chars {
        if !rules[&curr_ch].contains(&ch) {
            return false;
        }
        curr_ch = ch;
    }
    true
}

fn make_rules_map(rules: &str) -> HashMap<u8, Vec<u8>> {
    let lines = rules.lines();
    let mut map = HashMap::<u8, Vec<u8>>::new();
    for line in lines {
        let (lhs, rhs) = line.split_once(" > ").unwrap();
        let lhs = lhs.bytes().next().unwrap();
        map.insert(lhs, rhs.bytes().filter(|ch| *ch != b',').collect());
        map.entry(b'^')
            .and_modify(|list| list.push(lhs))
            .or_insert([lhs].to_vec());
    }
    map
}

fn remove_prefix(names: &mut Vec<&str>) {
    names.sort();
    names.dedup_by(|a, b| b.starts_with(*a));
}

pub struct Day7;

impl Solution for Day7 {
    const DAY: u32 = 7;

    fn part1(note: &str) -> impl Display {
        let (names, rules) = note.split_once("\n\n").unwrap();
        let names = names.split(",");
        let rules = make_rules_map(rules);

        let mut res = "";
        for name in names {
            if valid_name(name, &rules) {
                res = name;
            }
        }
        res
    }

    fn part2(note: &str) -> impl Display {
        let (names, rules) = note.split_once("\n\n").unwrap();
        let names = names.split(",");
        let rules = make_rules_map(rules);

        let mut res = 0;
        for (i, name) in names.enumerate() {
            if valid_name(name, &rules) {
                res += i + 1;
            }
        }

        res
    }

    fn part3(note: &str) -> impl Display {
        let (names, rules) = note.split_once("\n\n").unwrap();
        let names = names.split(",");
        let rules = make_rules_map(rules);
        let names = names.filter(|name| valid_name(name, &rules));
        let mut names = names.collect();
        remove_prefix(&mut names);

        let mut set = HashSet::new();
        for name in names {
            let mut list = VecDeque::new();
            list.push_back(name.to_string());
            while let Some(item) = list.pop_front() {
                if item.len() >= 7 {
                    set.insert(item.to_owned());
                }
                if item.len() >= 11 {
                    continue;
                }
                if let Some(char) = item.as_bytes().last()
                    && let Some(next) = rules.get(char)
                {
                    for b in next {
                        let mut new_item = item.to_string();
                        new_item.push(*b as char);
                        list.push_back(new_item);
                    }
                }
            }
        }

        set.len()
    }
}

#[cfg(test)]
mod test {
    use crate::utils::test;

    use super::*;

    #[test]
    fn part_1() {
        let test = r#" Oronris,Urakris,Oroneth,Uraketh

r > a,i,o
i > p,w
n > e,r
o > n,m
k > f,r
a > k
U > r
e > t
O > r
t > h
"#;

        assert_eq!(Day7::part1(test).to_string(), "Oroneth");
    }

    #[test]
    fn part_2() {
        let test = r#"Xanverax,Khargyth,Nexzeth,Helther,Braerex,Tirgryph,Kharverax

r > v,e,a,g,y
a > e,v,x,r
e > r,x,v,t
h > a,e,v
g > r,y
y > p,t
i > v,r
K > h
v > e
B > r
t > h
N > e
p > h
H > e
l > t
z > e
X > a
n > v
x > z
T > i"#;
        assert_eq!(Day7::part2(test).to_string(), "23");
    }

    #[test]
    fn part_3() {
        let test = r#"Xaryt

X > a,o
a > r,t
r > y,e,a
h > a,e,v
t > h
v > e
y > p,t"#;
        assert_eq!(Day7::part3(test).to_string(), "25");
    }

    #[test]
    fn part_3_larger() {
        let test = r#"Khara,Xaryt,Noxer,Kharax

r > v,e,a,g,y
a > e,v,x,r,g
e > r,x,v,t
h > a,e,v
g > r,y
y > p,t
i > v,r
K > h
v > e
B > r
t > h
N > e
p > h
H > e
l > t
z > e
X > a
n > v
x > z
T > i"#;
        assert_eq!(Day7::part3(test).to_string(), "1154")
    }

    #[test]
    fn part_1_real() {
        assert_eq!(Day7::part1(&test(7, 1)).to_string(), "Azmirath");
    }

    #[test]
    fn part_2_real() {
        assert_eq!(Day7::part2(&test(7, 2)).to_string(), "1956");
    }

    #[test]
    fn part_3_real() {
        assert_eq!(Day7::part3(&test(7, 3)).to_string(), "1783360");
    }
}
