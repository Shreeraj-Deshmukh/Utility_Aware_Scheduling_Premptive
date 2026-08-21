"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.660058, 'e_o_k': [1.291156, 1.032925], 'p_i': 10, 'u_i': 3.8713},
        {'id': 1, 'e_m': 2.227363, 'e_o_k': [1.732393, 1.385915], 'p_i': 20, 'u_i': 1.2249},
        {'id': 2, 'e_m': 3.200608, 'e_o_k': [2.489362, 1.991490], 'p_i': 40, 'u_i': 3.9801},
        {'id': 3, 'e_m': 0.045073, 'e_o_k': [0.017104, 0.013683, 0.010947, 0.008757, 0.007006, 0.005605], 'p_i': 80, 'u_i': 1.7372},
        {'id': 4, 'e_m': 2.908664, 'e_o_k': [1.103773, 0.883019, 0.706415, 0.565132, 0.452106, 0.361684], 'p_i': 10, 'u_i': 1.2016},
        {'id': 5, 'e_m': 1.511811, 'e_o_k': [1.175853, 0.940682], 'p_i': 10, 'u_i': 4.7805},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
