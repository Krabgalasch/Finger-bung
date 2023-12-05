import numpy as np

def fair_sharer(values, num_iterations, share=0.1):
    values_new = np.array(values)  # Convert to NumPy array
    counter = 0

    while counter <= num_iterations - 1:
        print(f'Old values:{values_new}')
        share_value = np.max(values_new) * share

        max_value_idx = np.argmax(values_new)

        new_max_value = np.max(values_new) - (share_value * 2)
        left_neighbor = values_new[max_value_idx - 1] + share_value
        right_neighbor = values_new[max_value_idx + 1] + share_value

        values_new[max_value_idx - 1] = left_neighbor
        values_new[max_value_idx + 1] = right_neighbor
        values_new[max_value_idx] = new_max_value
        counter += 1
        print(f'Your new values:{values_new}')

    return values_new

fair_sharer([0, 1000, 800, 0], 1) # [100, 800, 900, 0]
fair_sharer([0, 1000, 800, 0], 2) # [100, 890, 720, 90]

"""
def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.

    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """
    values_new = np.array(values) 
    counter = 0
    while counter <= num_iterations - 1:
        print(f'Old values:{values_new}')
        share_value = max(values) * share

        max_value_idx = values.index(max(values))

        new_max_value = max(values) - (share_value * 2)
        left_neighbor = values[max_value_idx - 1] + share_value
        right_neighbor = values[max_value_idx + 1] + share_value

        #print(max_value_idx - 1)
        #print(left_neighbor)

        values_new[max_value_idx - 1] = left_neighbor #Update value for left neighbor of the highest value 
        values_new[max_value_idx + 1] = right_neighbor #Update value for right neighbor of the highest value
        values_new[max_value_idx] = new_max_value
        counter += 1
        print(f'Your new values:{values_new}')
    return  values_new, print("\n\n")
"""

