use crate::utils::{Solution, read_text, test};
use std::{
    fmt::Display,
    ops::{Add, AddAssign, Div, DivAssign, Mul, MulAssign},
    path::PathBuf,
};

#[derive(Clone, Copy)]
struct ComplexNumber(i64, i64);

impl Display for ComplexNumber {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "[{},{}]", self.0, self.1)
    }
}

impl Add for ComplexNumber {
    type Output = Self;

    fn add(self, rhs: Self) -> Self::Output {
        Self(self.0 + rhs.0, self.1 + rhs.1)
    }
}

impl AddAssign for ComplexNumber {
    fn add_assign(&mut self, rhs: Self) {
        *self = *self + rhs
    }
}

impl Mul for ComplexNumber {
    type Output = ComplexNumber;

    fn mul(self, rhs: Self) -> Self::Output {
        ComplexNumber(
            self.0 * rhs.0 - self.1 * rhs.1,
            self.0 * rhs.1 + self.1 * rhs.0,
        )
    }
}

impl MulAssign for ComplexNumber {
    fn mul_assign(&mut self, rhs: Self) {
        *self = *self * rhs
    }
}

impl Div for ComplexNumber {
    type Output = Self;

    fn div(self, rhs: Self) -> Self::Output {
        Self(self.0 / rhs.0, self.1 / rhs.1)
    }
}

impl DivAssign for ComplexNumber {
    fn div_assign(&mut self, rhs: Self) {
        *self = *self / rhs
    }
}

fn check(x: ComplexNumber) -> bool {
    let mut r = ComplexNumber(0, 0);
    let div = ComplexNumber(100000, 100000);
    for _ in 0..100 {
        r *= r;
        r /= div;
        r += x;
        if r.0.abs() > 1000000 || r.1.abs() > 1000000 {
            return false;
        }
    }
    true
}

pub struct Day2;

impl Day2 {
    fn get_test(file: PathBuf) -> (i64, i64) {
        let s = read_text(file).unwrap();
        let mut it = s
            .trim_start_matches("A=[")
            .trim_end_matches("]")
            .split(",")
            .map(|c| c.parse::<i64>().unwrap());
        (it.next().unwrap(), it.next().unwrap())
    }
}

impl Solution for Day2 {
    fn part1() -> String {
        let (x, y) = Self::get_test(test(2, 1));
        let a = ComplexNumber(x, y);
        let mut r = ComplexNumber(0, 0);
        let div = ComplexNumber(10, 10);
        for _ in 0..3 {
            r *= r;
            r /= div;
            r += a;
        }

        r.to_string()
    }

    fn part2() -> String {
        let (x, y) = Self::get_test(test(2, 2));

        let mut count = 0;
        for i in 0..101 {
            for j in 0..101 {
                if check(ComplexNumber(x + 10 * i, y + 10 * j)) {
                    count += 1;
                }
            }
        }

        count.to_string()
    }

    fn part3() -> String {
        let (x, y) = Self::get_test(test(2, 2));

        let mut count = 0;
        for i in 0..1001 {
            for j in 0..1001 {
                if check(ComplexNumber(x + i, y + j)) {
                    count += 1;
                }
            }
        }

        count.to_string()
    }
}
