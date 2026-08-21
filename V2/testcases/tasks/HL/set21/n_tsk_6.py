"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.950986, 'e_o_k': [0.161075, 0.128860, 0.103088, 0.082470], 'p_i': 10, 'u_i': 1.4304},
        {'id': 1, 'e_m': 4.937204, 'e_o_k': [0.734353, 0.587483, 0.469986, 0.375989, 0.300791], 'p_i': 20, 'u_i': 2.0301},
        {'id': 2, 'e_m': 6.848037, 'e_o_k': [1.018568, 0.814854, 0.651884, 0.521507, 0.417205], 'p_i': 40, 'u_i': 4.4775},
        {'id': 3, 'e_m': 11.426349, 'e_o_k': [1.548588, 1.238870, 0.991096, 0.792877, 0.634302, 0.507441], 'p_i': 80, 'u_i': 1.0830},
        {'id': 4, 'e_m': 6.813635, 'e_o_k': [1.892677, 1.514141], 'p_i': 80, 'u_i': 1.9156},
        {'id': 5, 'e_m': 4.707239, 'e_o_k': [0.637962, 0.510369, 0.408296, 0.326636, 0.261309, 0.209047], 'p_i': 80, 'u_i': 2.8864},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
