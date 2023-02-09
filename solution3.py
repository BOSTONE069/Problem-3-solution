#!/usr/bin/env python3

def max_power(fields, towers):
    """
    It sorts the fields and towers, then iterates through them, keeping track of the maximum distance between a field and a
    tower

    :param fields: a list of integers representing the locations of the fields
    :param towers: a list of tower locations
    :return: The maximum distance between a field and a tower.
    """
    fields.sort()
    towers.sort()
    i = j = max_dist = 0
    while i < len(fields) and j < len(towers):
        if abs(fields[i] - towers[j]) > max_dist:
            max_dist = abs(fields[i] - towers[j])
        if fields[i] < towers[j]:
            i += 1
        else:
            j += 1
    return max_dist
