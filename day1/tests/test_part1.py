from typing import Any

from day1.part_1 import calculate_zero_counter


def test_example_rotations() -> None:
    rotations: list[str] = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]
    assert calculate_zero_counter(rotations) == 3


def test_full_rotation_right() -> None:
    rotations: list[str] = ["R100"]
    assert calculate_zero_counter(rotations) == 0


def test_multiple_zero_crossings() -> None:
    rotations: list[str] = ["R50", "R100"]
    assert calculate_zero_counter(rotations) == 2


def test_left_to_zero() -> None:
    rotations: list[str] = ["L50"]
    assert calculate_zero_counter(rotations) == 1


def test_no_rotations() -> None:
    rotations: list[Any] = []
    assert calculate_zero_counter(rotations) == 0
