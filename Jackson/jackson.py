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


def get_longest_time(duration_list: np.ndarray, start_time: np.ndarray, time: int) -> int:
    """Fuction that return longest of current posible tasks

    Parameters
    ----------
    duration_list : np.ndarray
        Duration time of all tasks
    start_time : np.ndarray
        Time when tasks can start
    time : int
        Sum of all druietion times

    Returns
    -------
    int
        Longest duration time

    >>> longest(duration_list, start_time, 30)
    20
    """
    # taking a start_time list of longest avalible tasks
    a= start_time[np.where(
        max(duration_list[np.where(start_time <= time)])
        == duration_list)[0]]

    # resturn index of the earliest task 
    return np.where(min(a) == start_time)[0][0]

def jackson(file_name: str) -> int:
    """Implementation of Micheal Jackson algorithm

    Parameters
    ----------
    file_name : str
        File name

    Returns
    -------
    int
        Duration time of all task in order
    >>> jackson("JACK1.DAT")
    31
    """
    # list of start times and duration times of tasks, stored as nested lists [[start_time],[duration_list]]
    task_data = get_task_data(file_name)
    # list of tasks start times
    start_time = task_data[:, 0]
    # list of tasks duration times
    duration_list = task_data[:, 1]
    # total duration of tasks completion
    time = min(start_time)

    while start_time.size != 0:
        if duration_list[np.where(start_time <= time)].size != 0:
            # take the longest task
            max_value = get_longest_time(duration_list, start_time, time)
            # adds time of completing another task to the whole process duration
            time = time + duration_list[max_value]
            # removes start time of already completed task from the task list
            start_time = np.delete(start_time, max_value)
            # removes corresponding duration of completed task from the task list
            duration_list = np.delete(duration_list, max_value)
        else:
            # takes us to the nearest task when there is now avalibe task
            time = min(start_time)
    return time
