"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.560596, 'e_o_k': [0.140149, 0.140149], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 2.273229, 'e_o_k': [0.189436, 0.189436, 0.189436, 0.189436, 0.189436, 0.189436], 'p_i': 20, 'u_i': 4.6964},
        {'id': 2, 'e_m': 5.286614, 'e_o_k': [0.881102, 0.881102, 0.881102], 'p_i': 40, 'u_i': 4.6519},
        {'id': 3, 'e_m': 1.840129, 'e_o_k': [0.460032, 0.460032], 'p_i': 80, 'u_i': 4.9020},
        {'id': 4, 'e_m': 0.311968, 'e_o_k': [0.025997, 0.025997, 0.025997, 0.025997, 0.025997, 0.025997], 'p_i': 80, 'u_i': 1.1409},
        {'id': 5, 'e_m': 1.580366, 'e_o_k': [0.158037, 0.158037, 0.158037, 0.158037, 0.158037], 'p_i': 40, 'u_i': 1.3844},
        {'id': 6, 'e_m': 2.375437, 'e_o_k': [0.237544, 0.237544, 0.237544, 0.237544, 0.237544], 'p_i': 80, 'u_i': 3.8571},
        {'id': 7, 'e_m': 0.040206, 'e_o_k': [0.010051, 0.010051], 'p_i': 20, 'u_i': 3.6185},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
