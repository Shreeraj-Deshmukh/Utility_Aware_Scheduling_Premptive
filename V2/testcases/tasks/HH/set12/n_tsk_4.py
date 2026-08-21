"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.424729, 'e_o_k': [1.885901, 1.508720], 'p_i': 10, 'u_i': 2.3775},
        {'id': 1, 'e_m': 6.907231, 'e_o_k': [2.876643, 2.301314, 1.841052, 1.472841, 1.178273], 'p_i': 20, 'u_i': 3.1328},
        {'id': 2, 'e_m': 6.719434, 'e_o_k': [3.855413, 3.084330, 2.467464], 'p_i': 40, 'u_i': 3.5798},
        {'id': 3, 'e_m': 3.534374, 'e_o_k': [1.471955, 1.177564, 0.942051, 0.753641, 0.602913], 'p_i': 80, 'u_i': 2.6618},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
