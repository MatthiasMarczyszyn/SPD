import numpy as np
import pandas as pd

import jackson as jackson


def test_jacson():
    files = ["JACK1.DAT","JACK2.DAT", "JACK3.DAT", "JACK4.DAT", "JACK5.DAT", "JACK6.DAT", "JACK7.DAT",  "JACK8.DAT"]
    assert jackson.jackson(files[0]) == 31
    assert jackson.jackson(files[1]) == 580
    assert jackson.jackson(files[2]) == 907
    assert jackson.jackson(files[3]) == 1006
    assert jackson.jackson(files[4]) == 2355
    assert jackson.jackson(files[5]) == 2586
    assert jackson.jackson(files[6]) == 4942
    assert jackson.jackson(files[7]) == 5042


def test_get_task_data():
    test_file_name = r"test_file.txt"
    file_contents = r"""1 5
4 5
1 4
7 3
3 6
4 7
"""
    with open(test_file_name, "w") as f:
        f.write(file_contents)
    assert (jackson.get_task_data(test_file_name) == np.array(
        [[1, 5], [4, 5], [1, 4], [7, 3], [3, 6], [4, 7]])).all()


def test_longest_time():
    test_start_time = np.array([5,8,3,2,1,90])
    test_duration_time = np.array([4,5900,2,67,8,2])
    assert jackson.get_longest_time(test_duration_time,test_start_time,3) == 3
