use crate::utils::{Solution, read_lines, test};
use std::path::PathBuf;

#[derive(Debug, Clone, Copy)]
struct Segment {
    mid: u32,
    left: Option<u32>,
    right: Option<u32>,
}

impl Segment {
    #[inline]
    fn new(mid: u32) -> Self {
        Self {
            mid,
            left: None,
            right: None,
        }
    }

    #[inline]
    fn is_full(&self) -> bool {
        self.left.is_some() && self.right.is_some()
    }

    fn try_insert(&mut self, n: u32) -> bool {
        if self.is_full() {
            return false;
        }
        if self.left.is_none() && n < self.mid {
            self.left = Some(n);
            return true;
        }
        if self.right.is_none() && n > self.mid {
            self.right = Some(n);
            return true;
        }
        false
    }

    fn score(&self) -> u64 {
        format!(
            "{}{}{}",
            self.left.map_or(String::new(), |n| n.to_string()),
            self.mid,
            self.right.map_or(String::new(), |n| n.to_string())
        )
        .parse()
        .unwrap()
    }
}

impl PartialEq for Segment {
    fn eq(&self, other: &Self) -> bool {
        self.score() == other.score()
    }
}

impl Eq for Segment {}

impl PartialOrd for Segment {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Segment {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.score().cmp(&other.score())
    }
}

#[derive(Debug, Default)]
struct Spine {
    segments: Vec<Segment>,
}

impl PartialEq for Spine {
    fn eq(&self, other: &Self) -> bool {
        self.quality() == other.quality() && self.segments == other.segments
    }
}

impl Eq for Spine {}

impl PartialOrd for Spine {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Spine {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        if self.quality() == other.quality() {
            return self.segments.cmp(&other.segments);
        }
        self.quality().cmp(&other.quality())
    }
}

impl Spine {
    #[inline]
    fn with_capacity(cap: usize) -> Self {
        Self {
            segments: Vec::with_capacity(cap),
        }
    }

    fn insert(&mut self, n: u32) {
        for segment in &mut self.segments {
            if segment.try_insert(n) {
                return;
            }
        }
        self.segments.push(Segment::new(n));
    }

    fn from_iter<I: IntoIterator<Item = u32>>(iter: I) -> Self {
        let it = iter.into_iter();
        let (lower, _) = it.size_hint();
        let mut spine = Spine::with_capacity(lower);
        for n in it {
            spine.insert(n);
        }
        spine
    }

    fn quality(&self) -> u64 {
        let mut out = String::new();
        for seg in &self.segments {
            out.push_str(seg.mid.to_string().as_str());
        }
        out.parse().unwrap()
    }
}

pub struct Day5;

impl Day5 {
    fn get_test(file: PathBuf) -> Vec<String> {
        read_lines(file).unwrap()
    }
}

impl Solution for Day5 {
    fn part1() -> String {
        let data = Self::get_test(test(5, 1));
        let (_, nums) = data[0].split_once(":").unwrap();
        let spine = Spine::from_iter(nums.split(",").map(|s| s.parse().unwrap()));
        spine.quality().to_string()
    }

    fn part2() -> String {
        let data = Self::get_test(test(5, 2));
        let mut worst_sword = u64::MAX;
        let mut best_sword = 0u64;
        for line in data {
            let (_, nums) = line.split_once(":").unwrap();
            let spine = Spine::from_iter(nums.split(",").map(|s| s.parse().unwrap()));
            worst_sword = worst_sword.min(spine.quality());
            best_sword = best_sword.max(spine.quality());
        }
        (best_sword - worst_sword).to_string()
    }

    fn part3() -> String {
        let data = Self::get_test(test(5, 3));
        let mut swords: Vec<(Spine, u32)> = Vec::new();
        for line in data {
            let (id, nums) = line.split_once(":").unwrap();
            let spine = Spine::from_iter(nums.split(",").map(|s| s.parse().unwrap()));
            swords.push((spine, id.parse().unwrap()));
        }
        swords.sort();
        swords.reverse();
        swords
            .iter()
            .enumerate()
            .map(|(i, v)| (i + 1) as u64 * v.1 as u64)
            .sum::<u64>()
            .to_string()
    }
}
