"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.464668, 'e_o_k': [2.561695, 2.049356, 1.639485], 'p_i': 10, 'u_i': 2.7485},
        {'id': 1, 'e_m': 2.898867, 'e_o_k': [1.207286, 0.965829, 0.772663, 0.618131, 0.494504], 'p_i': 20, 'u_i': 3.8876},
        {'id': 2, 'e_m': 3.597911, 'e_o_k': [1.498416, 1.198733, 0.958986, 0.767189, 0.613751], 'p_i': 40, 'u_i': 1.4132},
        {'id': 3, 'e_m': 9.491363, 'e_o_k': [4.501324, 3.601059, 2.880847, 2.304678], 'p_i': 80, 'u_i': 3.6535},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
