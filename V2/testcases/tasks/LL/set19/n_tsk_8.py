"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199991, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.2, "value": "8"}
"""

_SPEC = '{"B": 55.199991, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.2, "value": "8"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.529710, 'e_o_k': [0.259097, 0.207278, 0.165822, 0.132658], 'p_i': 10, 'u_i': 1.9017},
        {'id': 1, 'e_m': 1.119012, 'e_o_k': [0.310837, 0.248669], 'p_i': 20, 'u_i': 4.1004},
        {'id': 2, 'e_m': 0.375318, 'e_o_k': [0.063570, 0.050856, 0.040685, 0.032548], 'p_i': 40, 'u_i': 2.6358},
        {'id': 3, 'e_m': 2.653251, 'e_o_k': [0.543699, 0.434959, 0.347967], 'p_i': 80, 'u_i': 4.3577},
        {'id': 4, 'e_m': 0.027963, 'e_o_k': [0.004736, 0.003789, 0.003031, 0.002425], 'p_i': 40, 'u_i': 4.2383},
        {'id': 5, 'e_m': 0.045505, 'e_o_k': [0.006768, 0.005415, 0.004332, 0.003465, 0.002772], 'p_i': 80, 'u_i': 1.1754},
        {'id': 6, 'e_m': 9.092843, 'e_o_k': [2.525790, 2.020632], 'p_i': 80, 'u_i': 2.9766},
        {'id': 7, 'e_m': 1.344054, 'e_o_k': [0.182157, 0.145725, 0.116580, 0.093264, 0.074611, 0.059689], 'p_i': 40, 'u_i': 4.8798},
    ]
    B_BUDGET = 55.199991
    return processors, tasks, B_BUDGET
