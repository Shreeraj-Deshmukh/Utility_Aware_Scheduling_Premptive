"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.318061, 'e_o_k': [0.079515, 0.079515], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 2.437651, 'e_o_k': [0.609413, 0.609413], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 1.991584, 'e_o_k': [0.199158, 0.199158, 0.199158, 0.199158, 0.199158], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 10.739727, 'e_o_k': [2.684932, 2.684932], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 1.836977, 'e_o_k': [0.153081, 0.153081, 0.153081, 0.153081, 0.153081, 0.153081], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 1.702926, 'e_o_k': [0.212866, 0.212866, 0.212866, 0.212866], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 2.860437, 'e_o_k': [0.357555, 0.357555, 0.357555, 0.357555], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 8.242902, 'e_o_k': [0.686909, 0.686909, 0.686909, 0.686909, 0.686909, 0.686909], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
