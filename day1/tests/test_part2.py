from typing import Any

from day1.part_2 import calculate_zero_counter_click


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
    assert calculate_zero_counter_click(rotations) == 6


def test_right_50_clicks_zero_once() -> None:
    # From 50, going right 50 steps should click 0 once (at position 0)
    rotations: list[str] = ["R50"]
    assert calculate_zero_counter_click(rotations) == 1


def test_left_50_clicks_zero_once() -> None:
    # From 50, going left 50 steps should click 0 once (at position 0)
    rotations: list[str] = ["L50"]
    assert calculate_zero_counter_click(rotations) == 1


def test_full_circle_right_clicks_zero() -> None:
    # Full rotation right should click 0 once during the rotation
    rotations: list[str] = ["R100"]
    assert calculate_zero_counter_click(rotations) == 1


def test_no_rotations():
    # No rotations means no clicks
    rotations: list[Any] = []
    assert calculate_zero_counter_click(rotations) == 0
