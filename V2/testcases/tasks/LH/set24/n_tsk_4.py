"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.291296, 'e_o_k': [0.110541, 0.088432, 0.070746, 0.056597, 0.045277, 0.036222], 'p_i': 10, 'u_i': 1.4017},
        {'id': 1, 'e_m': 2.259781, 'e_o_k': [0.857537, 0.686029, 0.548824, 0.439059, 0.351247, 0.280998], 'p_i': 20, 'u_i': 2.4636},
        {'id': 2, 'e_m': 6.298206, 'e_o_k': [2.986954, 2.389563, 1.911651, 1.529321], 'p_i': 40, 'u_i': 2.5536},
        {'id': 3, 'e_m': 8.034092, 'e_o_k': [6.248738, 4.998991], 'p_i': 80, 'u_i': 3.8458},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
