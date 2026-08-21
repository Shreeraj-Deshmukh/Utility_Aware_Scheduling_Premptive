"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.441716, 'e_o_k': [0.059865, 0.047892, 0.038313, 0.030651, 0.024521, 0.019617], 'p_i': 10, 'u_i': 2.3061},
        {'id': 1, 'e_m': 3.450901, 'e_o_k': [0.958584, 0.766867], 'p_i': 20, 'u_i': 3.0150},
        {'id': 2, 'e_m': 2.918010, 'e_o_k': [0.434021, 0.347217, 0.277773, 0.222219, 0.177775], 'p_i': 40, 'u_i': 1.0989},
        {'id': 3, 'e_m': 16.308239, 'e_o_k': [3.341852, 2.673482, 2.138785], 'p_i': 80, 'u_i': 1.3802},
        {'id': 4, 'e_m': 3.302699, 'e_o_k': [0.491239, 0.392991, 0.314393, 0.251514, 0.201212], 'p_i': 40, 'u_i': 2.4137},
        {'id': 5, 'e_m': 17.913011, 'e_o_k': [4.975836, 3.980669], 'p_i': 80, 'u_i': 1.6729},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
