"""
This module provides utility functions for manipulating and transforming the input data.

Imports:
    numpy as np: Provides numerical operations and data structures.
"""
import numpy as np

def transpose_and_swap(arr):
    """
    Transposes the input array and then swaps the elements within each cell.

    Args:
        arr (np.ndarray): The input array to be transposed and swapped.

    Returns:
        np.ndarray: The transposed and swapped array.
    """
    return np.array([[cell[::-1] for cell in row] for row in zip(*arr)])

def fold_first_row_over_along_line_number(plan_view: np.ndarray, underside_view: np.ndarray, line_number: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Folds the first row of the plan view over along the specified line number and updates the plan and underside views accordingly.

    Args:
        plan_view (np.ndarray): The plan view of the object.
        underside_view (np.ndarray): The underside view of the object.
        line_number (int): The line number along which to fold the first row of the plan view.

    Returns:
        Tuple[np.ndarray, np.ndarray]: The updated plan view and underside view.
    """
    if len(plan_view)  <= line_number:
        return [], []
    transformation_matrix = np.array([[-1, 1]])
    new_plan_view = np.concatenate([underside_view[:line_number][::-1]*transformation_matrix, plan_view[line_number*2:]])
    new_underside_view = np.concatenate([underside_view[line_number:], plan_view[:line_number][::-1][len(plan_view)-line_number:]*transformation_matrix])
    return new_plan_view, new_underside_view

def fold_first_row_under_along_line_number(plan_view: np.ndarray, underside_view: np.ndarray, line_number: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Folds the first row of the plan view under along the specified line number and updates the plan and underside views accordingly.

    Args:
        plan_view (np.ndarray): The plan view of the object.
        underside_view (np.ndarray): The underside view of the object.
        line_number (int): The line number along which to fold the first row of the plan view.

    Returns:
        Tuple[np.ndarray, np.ndarray]: The updated plan view and underside view.
    """
    if len(plan_view)  <= line_number:
        return [], []
    transformation_matrix = np.array([[-1, 1]])
    new_plan_view = np.concatenate([plan_view[line_number:], underside_view[:line_number][::-1][len(plan_view)-line_number:]*transformation_matrix])
    new_underside_view = np.concatenate([plan_view[:line_number][::-1]*transformation_matrix, underside_view[line_number*2:]])
    return new_plan_view, new_underside_view

def fold_first_column_over_along_line_number(plan_view: np.ndarray, underside_view: np.ndarray, line_number: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Folds the first column of the plan view over along the specified line number and updates the plan and underside views accordingly.

    Args:
        plan_view (np.ndarray): The plan view of the object.
        underside_view (np.ndarray): The underside view of the object.
        line_number (int): The line number along which to fold the first column of the plan view.

    Returns:
        Tuple[np.ndarray, np.ndarray]: The updated plan view and underside view.
    """
    if len(plan_view[0])  <= line_number:
        return [], []
    current_plan_view, current_underside_view = fold_first_row_under_along_line_number(transpose_and_swap(underside_view), transpose_and_swap(plan_view), line_number)
    new_plan_view = transpose_and_swap(current_underside_view)
    new_underside_view = transpose_and_swap(current_plan_view)
    return new_plan_view, new_underside_view

def fold_first_column_under_along_line_number(plan_view: np.ndarray, underside_view: np.ndarray, line_number: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Folds the first column of the plan view under along the specified line number and updates the plan and underside views accordingly.

    Args:
        plan_view (np.ndarray): The plan view of the object.
        underside_view (np.ndarray): The underside view of the object.
        line_number (int): The line number along which to fold the first column of the plan view.

    Returns:
        Tuple[np.ndarray, np.ndarray]: The updated plan view and underside view.
    """
    if len(plan_view[0])  <= line_number:
        return [], []
    current_plan_view, current_underside_view = fold_first_row_over_along_line_number(transpose_and_swap(underside_view), transpose_and_swap(plan_view), line_number)
    new_plan_view = transpose_and_swap(current_underside_view)
    new_underside_view = transpose_and_swap(current_plan_view)
    return new_plan_view, new_underside_view

def get_unique_number(view: np.ndarray) -> set:
    """
    Retrieves a set of unique absolute numbers from the input view.

    Args:
        view (np.ndarray): The input view.

    Returns:
        set: A set of unique numbers from the input view.
    """
    number_set = set()
    for row in view:
        for cell in row:
            number_set.add(abs(cell[0]))
    return number_set

def flip_the_view(view: np.ndarray) -> np.ndarray:
    """
    Flips the input view vertically.

    Args:
        view (np.ndarray): The input view to be flipped.

    Returns:
        np.ndarray: The flipped view.
    """
    view = view*np.array([[-1, 1]])
    return view[::-1]
