from day1.part_1 import calculate_zero_counter


def test_example_rotations():
    rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    assert calculate_zero_counter(rotations) == 3


def test_full_rotation_right():
    # R100 from 50 should land on 50 again, passing through 0 once
    rotations = ["R100"]
    assert calculate_zero_counter(rotations) == 0  # Ends at 50, not at 0


def test_multiple_zero_crossings():
    # R50 lands at 0, then R100 goes around and lands at 0 again
    rotations = ["R50", "R100"]
    assert calculate_zero_counter(rotations) == 2


def test_left_to_zero():
    # From 50, L50 should land exactly at 0
    rotations = ["L50"]
    assert calculate_zero_counter(rotations) == 1


def test_no_rotations():
    # No rotations means dial stays at starting position
    rotations = []
    assert calculate_zero_counter(rotations) == 0
