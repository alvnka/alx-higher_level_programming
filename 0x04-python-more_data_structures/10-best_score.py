#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        max_score_candidate = ''
        max_score = 0
        for key, value in a_dictionary.items():
            if value > max_score:
                max_score_candidate = key
                max_score = value
        return max_score_candidate
