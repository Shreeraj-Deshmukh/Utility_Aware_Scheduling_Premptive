"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.481803, 'e_o_k': [0.702752, 0.562202, 0.449761, 0.359809], 'p_i': 10, 'u_i': 2.9572},
        {'id': 1, 'e_m': 2.034934, 'e_o_k': [0.965077, 0.772062, 0.617649, 0.494119], 'p_i': 20, 'u_i': 4.0373},
        {'id': 2, 'e_m': 0.389490, 'e_o_k': [0.162210, 0.129768, 0.103815, 0.083052, 0.066441], 'p_i': 40, 'u_i': 2.8937},
        {'id': 3, 'e_m': 11.226863, 'e_o_k': [5.324393, 4.259514, 3.407612, 2.726089], 'p_i': 80, 'u_i': 3.5048},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
