"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.728311, 'e_o_k': [0.566464, 0.453171], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 3.236491, 'e_o_k': [2.517271, 2.013817], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 0.535015, 'e_o_k': [0.416123, 0.332898], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 4.750488, 'e_o_k': [3.694824, 2.955859], 'p_i': 80, 'u_i': 4.1202},
        {'id': 4, 'e_m': 0.182718, 'e_o_k': [0.142114, 0.113691], 'p_i': 40, 'u_i': 4.7898},
        {'id': 5, 'e_m': 0.092022, 'e_o_k': [0.071573, 0.057258], 'p_i': 10, 'u_i': 3.8151},
        {'id': 6, 'e_m': 2.641333, 'e_o_k': [2.054370, 1.643496], 'p_i': 40, 'u_i': 2.4922},
        {'id': 7, 'e_m': 0.127844, 'e_o_k': [0.099434, 0.079547], 'p_i': 10, 'u_i': 1.4417},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
