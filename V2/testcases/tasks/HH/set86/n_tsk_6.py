"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.140267, 'e_o_k': [0.053228, 0.042582, 0.034066, 0.027253, 0.021802, 0.017442], 'p_i': 10, 'u_i': 3.8731},
        {'id': 1, 'e_m': 0.613585, 'e_o_k': [0.352057, 0.281645, 0.225316], 'p_i': 20, 'u_i': 4.5676},
        {'id': 2, 'e_m': 3.794514, 'e_o_k': [1.799566, 1.439653, 1.151722, 0.921378], 'p_i': 40, 'u_i': 2.8991},
        {'id': 3, 'e_m': 22.763738, 'e_o_k': [9.480376, 7.584301, 6.067441, 4.853953, 3.883162], 'p_i': 80, 'u_i': 1.9490},
        {'id': 4, 'e_m': 2.089724, 'e_o_k': [1.625341, 1.300272], 'p_i': 20, 'u_i': 1.1516},
        {'id': 5, 'e_m': 10.855934, 'e_o_k': [6.228815, 4.983052, 3.986441], 'p_i': 40, 'u_i': 2.6742},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
