"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760003, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760003, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.131863, 'e_o_k': [0.010723, 0.008578, 0.006862, 0.005490, 0.004392, 0.003514], 'p_i': 10, 'u_i': 2.1335},
        {'id': 1, 'e_m': 0.427322, 'e_o_k': [0.034748, 0.027799, 0.022239, 0.017791, 0.014233, 0.011386], 'p_i': 20, 'u_i': 1.1307},
        {'id': 2, 'e_m': 2.238723, 'e_o_k': [0.199791, 0.159833, 0.127866, 0.102293, 0.081834], 'p_i': 40, 'u_i': 4.3260},
        {'id': 3, 'e_m': 1.203601, 'e_o_k': [0.147984, 0.118387, 0.094710], 'p_i': 80, 'u_i': 4.7000},
        {'id': 4, 'e_m': 0.469028, 'e_o_k': [0.078171, 0.062537], 'p_i': 10, 'u_i': 1.4843},
        {'id': 5, 'e_m': 0.896222, 'e_o_k': [0.149370, 0.119496], 'p_i': 20, 'u_i': 4.5666},
        {'id': 6, 'e_m': 3.122163, 'e_o_k': [0.278632, 0.222905, 0.178324, 0.142660, 0.114128], 'p_i': 10, 'u_i': 2.1776},
        {'id': 7, 'e_m': 7.240351, 'e_o_k': [0.890207, 0.712166, 0.569733], 'p_i': 80, 'u_i': 3.5354},
    ]
    B_BUDGET = 71.760003
    return processors, tasks, B_BUDGET
