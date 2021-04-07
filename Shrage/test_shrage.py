import shrage
import numpy as np
import pandas as pd


def test_get_task_data():
    test_file_name = r"test_file.txt"
#    file_contents = r"""1 5
#4 5
#1 4
#7 3
#3 6
#4 7
#"""
    with open(test_file_name, "w") as f:
        f.write(file_contents)
#    assert (rpq.get_task_data(test_file_name) == np.array(
#        [[1, 5], [4, 5], [1, 4], [7, 3], [3, 6], [4, 7]])).all()

def test_get_longest_time():
#    test_start_time = np.array([5,8,3,2,1,90])
#    test_duration_time = np.array([4,5900,2,67,8,2])
#    assert rpq.get_longest_time(test_duration_time,test_start_time,3) == 3


def test_schrage_problem():
    files = ["1.DAT", "2.DAT", "3.DAT"]
#    assert rpq.rpq_problem(files[0]) == 
