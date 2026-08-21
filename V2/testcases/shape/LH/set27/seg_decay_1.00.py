"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.707837, 'e_o_k': [0.597743, 0.597743, 0.597743, 0.597743], 'p_i': 10, 'u_i': 3.9517},
        {'id': 1, 'e_m': 0.074416, 'e_o_k': [0.020836, 0.020836, 0.020836, 0.020836, 0.020836], 'p_i': 20, 'u_i': 3.7467},
        {'id': 2, 'e_m': 1.043073, 'e_o_k': [0.292060, 0.292060, 0.292060, 0.292060, 0.292060], 'p_i': 40, 'u_i': 4.6120},
        {'id': 3, 'e_m': 0.422237, 'e_o_k': [0.295566, 0.295566], 'p_i': 80, 'u_i': 4.9202},
        {'id': 4, 'e_m': 0.946737, 'e_o_k': [0.662716, 0.662716], 'p_i': 80, 'u_i': 4.2451},
        {'id': 5, 'e_m': 0.544998, 'e_o_k': [0.381499, 0.381499], 'p_i': 10, 'u_i': 4.7909},
        {'id': 6, 'e_m': 1.274474, 'e_o_k': [0.446066, 0.446066, 0.446066, 0.446066], 'p_i': 10, 'u_i': 3.3523},
        {'id': 7, 'e_m': 0.014372, 'e_o_k': [0.005030, 0.005030, 0.005030, 0.005030], 'p_i': 40, 'u_i': 1.0347},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
