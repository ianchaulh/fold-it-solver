"""
This module provides a function for performing depth-first search (DFS) on a folding problem.

Imports:
    numpy as np: Provides numerical operations and data structures.
    func: Contains utility functions for manipulating and transforming the input data.
"""
import numpy as np
import func

BOARD = np.array([[[1, 1],[2, 2],[3, 3],[4, 4]],
                  [[5, 5],[6, 6],[7, 7],[8, 8]],
                  [[9, 9],[10, 10],[11, 11],[12, 12]],
                  [[13, 13],[14, 14],[15, 15],[16, 16]]])

global PATH, STEP
PATH, STEP = [], []

def dfs(plan_view: np.ndarray, underside_view: np.ndarray, target: set) -> bool:
    """
    Performs a depth-first search to find a sequence of folding operations that transforms the input paper from its plan view to the target shape.

    Args:
        plan_view (np.ndarray): The plan view of the input cloth.
        underside_view (np.ndarray): The underside view of the input cloth.
        target (set): The target set of items.

    Returns:
        bool: True if a sequence of folding operations is found, False otherwise.

    Raises:
        None
    """
    global PATH, STEP
    plan_view_set = func.get_unique_number(plan_view)
    underside_view_set = func.get_unique_number(underside_view)
    if plan_view_set == target:
        PATH.append(plan_view)
        STEP.insert(0, "Finish!")
        return True
    if underside_view_set == target:
        PATH.append(plan_view)
        PATH.append(func.flip_the_view(underside_view))
        STEP.insert(0, "Finish!")
        STEP.insert(0, "Flip 180 degree.")
        return True
    if (len(plan_view_set) == 0 or
        len(target) > len(plan_view_set) or
        not target.issubset(plan_view_set | underside_view_set)):
        return False
    PATH.append(plan_view)
    for i in range(1,4):
        res = dfs(func.fold_first_row_over_along_line_number(plan_view, underside_view, i)[0],
                  func.fold_first_row_over_along_line_number(plan_view, underside_view, i)[1],
                  target)
        if res:
            STEP.insert(0, f"Fold the first {i} row over along horizontal line {i}.")
            return True
    if not res:
        for i in range(1, 4):
            res = dfs(func.fold_first_row_under_along_line_number(plan_view, underside_view, i)[0],
                      func.fold_first_row_under_along_line_number(plan_view, underside_view, i)[1],
                      target)
            if res:
                STEP.insert(0, f"Fold the first {i} row under along horizontal line {i}.")
                return True
    if not res:
        for i in range(1, 4):
            res = dfs(func.fold_first_column_over_along_line_number(plan_view, underside_view, i)[0],
                      func.fold_first_column_over_along_line_number(plan_view, underside_view, i)[1],
                      target)
            if res:
                STEP.insert(0, f"Fold the first {i} column over along vertical line {i}.")
                return True
    if not res:
        for i in range(1, 4):
            res = dfs(func.fold_first_column_under_along_line_number(plan_view, underside_view, i)[0],
                      func.fold_first_column_under_along_line_number(plan_view, underside_view, i)[1],
                      target)
            if res:
                STEP.insert(0, f"Fold the first {i} column under along vertical line {i}.")
                return True
    PATH.pop()
    return False
