import numpy as np
import pandas as pd


def get_task_data(file_name: str) -> np.ndarray:
    """Function that reurns data from file as ndarray

    Parameters
    ----------
    file_name : str
        File name

    Returns
    -------
    np.ndarray
        Data form file in ndarray
    >>> get_task_data("george_floyd.txt")
    array([1, 2, 3, 4])
    """
    return pd.read_csv(file_name, delimiter=" ", header=None).to_numpy()


def get_longest_time(r: np.ndarray, current_time: int) -> int:
    """Fuction that return longest of current posible tasks

    Parameters
    ----------
    p : np.ndarray
        Duration current_time of all tasks
    r : np.ndarray
        Time when tasks can start
    current_time : int
        Sum of all druietion times

    Returns
    -------
    int
        Longest duration current_time

    >>> longest(r, p, 30)
    20
    """
    # taking a r list of longest avalible tasks
    

    # resturn index of the earliest task
    return np.where(min(r) == r)[0][0]


def rpq_problem(file_name):
    task_data = get_task_data(file_name)
    r = task_data[:, 0]
    p = task_data[:, 1]
    q = task_data[:, 2]
    end_time = 0
    current_time = r[np.where(max(r) == r)[0][0]] - np.sum([x for x in p if np.where(x == p)[0][0] != np.where(max(r) == r)[0][0]])
    if(current_time<0): current_time = 0 
    while r.size != 0:
        if p[np.where(r <= current_time)].size != 0:
            # take the longest task
            max_value = get_longest_time(r, current_time)
            # adds current_time of completing another task to the whole process duration
            current_time = current_time + p[max_value]
            # adds end_time t
            if current_time > end_time:
                end_time = current_time + q[max_value]
            elif current_time + q[max_value] < end_time:
                end_time = end_time
            else:
                end_time = end_time + q[max_value]
            # printing removed values
           # print(f"{r[max_value]} {p[max_value]} {q[max_value]}")
            # removes corresponding availability time of completed task from the task list
            r = np.delete(r, max_value)
            # removes corresponding duration of completed task from the task list
            p = np.delete(p, max_value)
            # removes corresponding delivery time of completed task from the task list
            q = np.delete(q, max_value)
            # takes us to the nearest task when there is now avalibe task
        else:
            current_time = min(r)
    return end_time

files = ["1.DAT", "2.DAT", "3.DAT", "4.DAT", "5.DAT", "6.DAT", "7.DAT", "8.DAT", "9.DAT"]

for file in files:
    print(rpq_problem(file))
