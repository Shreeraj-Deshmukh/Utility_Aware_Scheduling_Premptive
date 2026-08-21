"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.697259, 'e_o_k': [0.330678, 0.264543, 0.211634, 0.169307], 'p_i': 10, 'u_i': 1.6266},
        {'id': 1, 'e_m': 0.828822, 'e_o_k': [0.644639, 0.515711], 'p_i': 20, 'u_i': 2.5167},
        {'id': 2, 'e_m': 15.359768, 'e_o_k': [5.828692, 4.662953, 3.730363, 2.984290, 2.387432, 1.909946], 'p_i': 40, 'u_i': 3.7793},
        {'id': 3, 'e_m': 24.387107, 'e_o_k': [11.565701, 9.252561, 7.402049, 5.921639], 'p_i': 80, 'u_i': 1.9533},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
