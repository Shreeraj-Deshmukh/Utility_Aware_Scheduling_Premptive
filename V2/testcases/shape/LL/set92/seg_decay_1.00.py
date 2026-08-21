"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200033, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200033, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.279536, 'e_o_k': [0.027954, 0.027954, 0.027954, 0.027954, 0.027954], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 0.807491, 'e_o_k': [0.067291, 0.067291, 0.067291, 0.067291, 0.067291, 0.067291], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 3.179023, 'e_o_k': [0.529837, 0.529837, 0.529837], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 7.775197, 'e_o_k': [0.971900, 0.971900, 0.971900, 0.971900], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.001832, 'e_o_k': [0.000458, 0.000458], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 1.937647, 'e_o_k': [0.322941, 0.322941, 0.322941], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 0.361320, 'e_o_k': [0.045165, 0.045165, 0.045165, 0.045165], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 3.778825, 'e_o_k': [0.472353, 0.472353, 0.472353, 0.472353], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 55.200033
    return processors, tasks, B_BUDGET
