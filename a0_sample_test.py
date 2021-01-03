"""CSC148 Assignment 0: Sample tests

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Assignment 0.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests and to be confident your code is correct.

Note: this file is to only help you; you will not submit it when you hand in
the assignment.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Mario Badr, Christine Murad, Diane Horton, Misha Schwartz, Sophia Huynh
and Jaisie Sin

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Christine Murad, Diane Horton, Misha Schwartz,
Sophia Huynh and Jaisie Sin
"""
from datetime import datetime
from gym import WorkoutClass, Instructor, Gym


def test_instructor_attributes() -> None:
    """Test the public attributes of a new instructor."""
    instructor = Instructor(5, 'Matthew')
    assert instructor.get_id() == 5
    assert instructor.name == 'Matthew'


def test_instructor_one_certificate_get_certificates() -> None:
    """Test Instructor.get_num_certificates with a single certificate."""
    instructor = Instructor(5, 'Matthew')
    assert instructor.add_certificate('Kickboxing')
    assert instructor.get_num_certificates() == 1


def test_instructor_one_certificate_can_teach() -> None:
    """Test Instructor.can_teach with a single satisfying certificate."""
    instructor = Instructor(5, 'Matthew')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    assert instructor.add_certificate('Lifeguard')
    assert instructor.can_teach(swimming)


def test_instructor_many_certificate_can_teach_JEN() -> None:
    """Test Instructor.can_teach with more than necessary amount of certificates."""
    instructor = Instructor(5, 'Matthew')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    assert instructor.add_certificate('Lifeguard')
    assert instructor.add_certificate('Cross Fit')
    assert instructor.add_certificate('Personal Trainer')
    assert instructor.can_teach(swimming)


def test_instructor_one_certificate_cannot_teach_JEN() -> None:
    instructor = Instructor(5, 'Matthew')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    assert instructor.add_certificate('Cross Fit')
    assert not instructor.can_teach(swimming)


def test_schedule_in_unavailable_room_JEN() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    assert ac.add_instructor(instructor)
    instructor2 = Instructor(6, 'Jennifer')
    assert ac.add_instructor(instructor2)
    assert ac.add_room('25-yard Pool', 100)
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    assert ac.add_workout_class(swimming)
    assert instructor.add_certificate('Lifeguard')
    assert instructor2.add_certificate('Lifeguard')
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert not ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                 swimming.get_name(), instructor2.get_id())

def test_schedule_unqualified_instructor_JEN() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    assert ac.add_instructor(instructor)
    assert ac.add_room('25-yard Pool', 100)
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    assert ac.add_workout_class(swimming)
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert not ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())


def test_instr_teaching_other_class_JEN() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    assert ac.add_instructor(instructor)
    assert ac.add_room('25-yard Pool', 100)
    assert ac.add_room('Weight Room', 100)
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    crossfit = WorkoutClass('Cross Fit', [])
    assert instructor.add_certificate('Lifeguard')
    assert ac.add_workout_class(swimming)
    assert ac.add_workout_class(crossfit)
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert not ac.schedule_workout_class(jan_28_2020_11_00, 'Weight Room',
                                     crossfit.get_name(), instructor.get_id())


def test_gym_register_one_class() -> None:
    """Test Gym.register with a single user and class."""
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert instructor.add_certificate('Lifeguard')
    assert ac.add_workout_class(swimming)
    assert ac.add_instructor(instructor)
    assert ac.add_room('25-yard Pool', 100)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert ac.register(jan_28_2020_11_00, 'Benjamin', 'Swimming')


def test_gym_register_many_classes_JEN() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    instructor2 = Instructor(15, 'Jennifer')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    crossfit = WorkoutClass('Cross Fit', ['Cross Fit'])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert instructor.add_certificate('Lifeguard')
    assert instructor2.add_certificate('Cross Fit')
    assert ac.add_workout_class(swimming)
    assert ac.add_workout_class(crossfit)
    assert ac.add_instructor(instructor)
    assert ac.add_instructor(instructor2)
    assert ac.add_room('25-yard Pool', 100)
    assert ac.add_room('Weight Room', 100)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert ac.schedule_workout_class(jan_28_2020_11_00, 'Weight Room',
                                     crossfit.get_name(), instructor2.get_id())
    assert ac.register(jan_28_2020_11_00, 'Benjamin', 'Swimming')
    assert not ac.register(jan_28_2020_11_00, 'Benjamin', 'Cross Fit')

def test_register_no_room_left_with_that_class_JEN() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    instructor2 = Instructor(15, 'Jennifer')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    crossfit = WorkoutClass('Cross Fit', ['Cross Fit'])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert instructor.add_certificate('Lifeguard')
    assert instructor2.add_certificate('Cross Fit')
    assert ac.add_workout_class(swimming)
    assert ac.add_workout_class(crossfit)
    assert ac.add_instructor(instructor)
    assert ac.add_instructor(instructor2)
    assert ac.add_room('25-yard Pool', 1)
    assert ac.add_room('Weight Room', 1)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert ac.schedule_workout_class(jan_28_2020_11_00, 'Weight Room',
                                     crossfit.get_name(), instructor2.get_id())
    assert ac.register(jan_28_2020_11_00, 'Benjamin', 'Swimming')
    assert not ac.register(jan_28_2020_11_00, 'Eric', 'Swimming')

def test_register_no_room_left_move_to_other_room_JEN() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    instructor2 = Instructor(15, 'Jennifer')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert instructor.add_certificate('Lifeguard')
    assert instructor2.add_certificate('Lifeguard')
    assert ac.add_workout_class(swimming)
    assert ac.add_instructor(instructor)
    assert ac.add_instructor(instructor2)
    assert ac.add_room('25-yard Pool', 1)
    assert ac.add_room('Weight Room', 1)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                 swimming.get_name(), instructor.get_id())
    assert ac.schedule_workout_class(jan_28_2020_11_00, 'Weight Room',
                                 swimming.get_name(), instructor2.get_id())
    assert ac.register(jan_28_2020_11_00, 'Benjamin', 'Swimming')

def test_gym_offerings_at_one_class() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert instructor.add_certificate('Lifeguard')
    assert ac.add_workout_class(swimming)
    assert ac.add_instructor(instructor)
    assert ac.add_room('25-yard Pool', 100)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert ac.offerings_at(jan_28_2020_11_00) == \
        [('Matthew', 'Swimming', '25-yard Pool')]

def test_gym_no_offerings_JEN() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    feb_28_2020_11_00 = datetime(2020, 2, 28, 11, 0)
    t1 = datetime(2020, 1, 29, 11, 0)
    assert instructor.add_certificate('Lifeguard')
    assert ac.add_workout_class(swimming)
    assert ac.add_instructor(instructor)
    assert ac.add_room('25-yard Pool', 100)
    assert ac.schedule_workout_class(t1, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert ac.offerings_at(feb_28_2020_11_00) == []

def test_gym_offerings_at_one_class_same_workouts_JEN() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    instructor2 = Instructor(12, 'Jennifer')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert instructor.add_certificate('Lifeguard')
    assert instructor2.add_certificate('Lifeguard')
    assert ac.add_workout_class(swimming)
    assert ac.add_instructor(instructor)
    assert ac.add_instructor(instructor2)
    assert ac.add_room('25-yard Pool', 100)
    assert ac.add_room('Kiddie Pool', 100)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert ac.schedule_workout_class(jan_28_2020_11_00, 'Kiddie Pool',
                                     swimming.get_name(), instructor2.get_id())
    assert ac.offerings_at(jan_28_2020_11_00) == \
           [('Matthew', 'Swimming', '25-yard Pool'), ('Jennifer', 'Swimming', 'Kiddie Pool')]


def test_instructor_hours_two_people_mixed_hours_JEN() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    instructor2 = Instructor(12, 'Jennifer')
    swimming = WorkoutClass('Swimming', [])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    jan_28_2020_12_00 = datetime(2020, 1, 29, 12, 0)
    assert ac.add_workout_class(swimming)
    assert ac.add_instructor(instructor)
    assert ac.add_instructor(instructor2)
    assert ac.add_room('25-yard Pool', 100)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert ac.schedule_workout_class(jan_28_2020_12_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    t1 = datetime(2020, 1, 29, 11, 0)
    t2 = datetime(2020, 1, 29, 12, 0)
    assert ac.instructor_hours(t1, t2) == {5: 2, 12: 0}


def test_gym_one_instructor_one_hour_pay_no_certificates() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    swimming = WorkoutClass('Swimming', [])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert ac.add_workout_class(swimming)
    assert ac.add_instructor(instructor)
    assert ac.add_room('25-yard Pool', 100)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    t1 = datetime(2020, 1, 17, 11, 0)
    t2 = datetime(2020, 1, 29, 13, 0)
    assert ac.payroll(t1, t2, 22.0) == [(5, 'Matthew', 1, 22)]


def test_gym_many_instructors_mixed_hours_mixed_certificates_JEN() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    instructor2 = Instructor(12, 'Jennifer')
    swimming = WorkoutClass('Swimming', [])
    crossfit = WorkoutClass('Cross Fit', ['Cross Fit'])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    jan_28_2020_12_00 = datetime(2020, 1, 29, 12, 0)
    assert ac.add_workout_class(swimming)
    assert ac.add_workout_class(crossfit)
    assert ac.add_instructor(instructor)
    assert ac.add_instructor(instructor2)
    assert instructor2.add_certificate('Cross Fit')
    assert ac.add_room('25-yard Pool', 100)
    assert ac.add_room('Weight Room', 50)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert ac.schedule_workout_class(jan_28_2020_11_00, 'Weight Room',
                                     crossfit.get_name(), instructor2.get_id())
    assert ac.schedule_workout_class(jan_28_2020_12_00, 'Weight Room',
                                     crossfit.get_name(), instructor2.get_id())
    t1 = datetime(2020, 1, 17, 11, 0)
    t2 = datetime(2020, 1, 29, 13, 0)
    assert ac.payroll(t1, t2, 22.0) == [(5, 'Matthew', 1, 22.0), (12, 'Jennifer', 2, 47.0)]


if __name__ == '__main__':
    import pytest
    pytest.main(['a0_sample_test.py'])
