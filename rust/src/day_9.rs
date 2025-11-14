use crate::utils::Solution;

pub struct Day9;

impl Solution for Day9 {
    const DAY: u32 = 9;

    fn part1(note: &str) -> impl std::fmt::Display {
        let mems = note
            .lines()
            .map(|l| l.split_once(":").unwrap())
            .map(|(_, dna)| dna.as_bytes())
            .collect::<Vec<&[u8]>>();

        for i in 0..mems.len() {
            for j in 0..mems.len() {
                if i == j {
                    continue;
                }
                for k in 0..mems.len() {
                    if j == k || i == k {
                        continue;
                    }

                    if let Some(degree) = similarity(mems[i], mems[j], mems[k]) {
                        return degree;
                    }
                }
            }
        }

        0
    }

    fn part2(note: &str) -> impl std::fmt::Display {
        let mems = note
            .lines()
            .map(|l| l.split_once(":").unwrap())
            .map(|(_, dna)| dna.as_bytes())
            .collect::<Vec<&[u8]>>();

        let mut res = 0;

        for i in 0..mems.len() {
            for j in 0..(mems.len() - 1) {
                if i == j {
                    continue;
                }
                for k in (j + 1)..mems.len() {
                    if j == k || i == k {
                        continue;
                    }

                    if let Some(degree) = similarity(mems[i], mems[j], mems[k]) {
                        res += degree;
                    }
                }
            }
        }

        res
    }

    fn part3(note: &str) -> impl std::fmt::Display {
        todo!()
    }
}

fn similarity(child: &[u8], p1: &[u8], p2: &[u8]) -> Option<u32> {
    let mut a = 0;
    let mut b = 0;
    for (i, c) in child.iter().enumerate() {
        if *c != p1[i] && *c != p2[i] {
            return None;
        }
        if *c == p1[i] {
            a += 1;
        }

        if *c == p2[i] {
            b += 1;
        }
    }

    Some(a * b)
}

#[cfg(test)]
mod test {
    use crate::utils::test;

    use super::*;

    #[test]
    fn part_1() {
        let test = r"1:CAAGCGCTAAGTTCGCTGGATGTGTGCCCGCG
2:CTTGAATTGGGCCGTTTACCTGGTTTAACCAT
3:CTAGCGCTGAGCTGGCTGCCTGGTTGACCGCG";
        assert_eq!(Day9::part1(test).to_string(), "414")
    }

    #[test]
    fn part_1_real() {
        assert_eq!(Day9::part1(&test(9, 1)).to_string(), "6308")
    }

    #[test]
    fn part_2() {
        let test = r"1:GCAGGCGAGTATGATACCCGGCTAGCCACCCC
2:TCTCGCGAGGATATTACTGGGCCAGACCCCCC
3:GGTGGAACATTCGAAAGTTGCATAGGGTGGTG
4:GCTCGCGAGTATATTACCGAACCAGCCCCTCA
5:GCAGCTTAGTATGACCGCCAAATCGCGACTCA
6:AGTGGAACCTTGGATAGTCTCATATAGCGGCA
7:GGCGTAATAATCGGATGCTGCAGAGGCTGCTG";
        assert_eq!(Day9::part2(test).to_string(), "1245");
    }

    #[test]
    fn part_2_real() {
        assert_eq!(Day9::part2(&test(9, 2)).to_string(), "1245");
    }
}
