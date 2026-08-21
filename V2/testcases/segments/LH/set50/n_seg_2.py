"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319992, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319992, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.597822, 'e_o_k': [0.464973, 0.371978], 'p_i': 10, 'u_i': 1.3138},
        {'id': 1, 'e_m': 0.537328, 'e_o_k': [0.417922, 0.334337], 'p_i': 20, 'u_i': 3.5906},
        {'id': 2, 'e_m': 1.853768, 'e_o_k': [1.441819, 1.153456], 'p_i': 40, 'u_i': 2.7107},
        {'id': 3, 'e_m': 4.965351, 'e_o_k': [3.861940, 3.089552], 'p_i': 80, 'u_i': 4.0673},
        {'id': 4, 'e_m': 0.125857, 'e_o_k': [0.097889, 0.078311], 'p_i': 10, 'u_i': 2.2713},
        {'id': 5, 'e_m': 0.986987, 'e_o_k': [0.767656, 0.614125], 'p_i': 80, 'u_i': 2.2740},
        {'id': 6, 'e_m': 11.937053, 'e_o_k': [9.284374, 7.427499], 'p_i': 80, 'u_i': 2.9164},
        {'id': 7, 'e_m': 1.232163, 'e_o_k': [0.958349, 0.766679], 'p_i': 40, 'u_i': 4.5766},
    ]
    B_BUDGET = 88.319992
    return processors, tasks, B_BUDGET
