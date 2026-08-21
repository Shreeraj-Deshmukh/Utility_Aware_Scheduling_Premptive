"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.015283, 'e_o_k': [0.220178, 0.132107, 0.079264, 0.047558, 0.028535], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 1.338137, 'e_o_k': [0.280725, 0.168435, 0.101061, 0.060637, 0.036382, 0.021829], 'p_i': 20, 'u_i': 2.4707},
        {'id': 2, 'e_m': 1.215369, 'e_o_k': [0.254970, 0.152982, 0.091789, 0.055073, 0.033044, 0.019826], 'p_i': 40, 'u_i': 1.1046},
        {'id': 3, 'e_m': 11.427473, 'e_o_k': [3.571085, 2.142651], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 4.192750, 'e_o_k': [0.963408, 0.578045, 0.346827, 0.208096], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.541048, 'e_o_k': [0.124322, 0.074593, 0.044756, 0.026853], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 5.660701, 'e_o_k': [1.768969, 1.061381], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.655144, 'e_o_k': [0.204732, 0.122839], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
