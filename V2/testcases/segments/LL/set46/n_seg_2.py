"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.418756, 'e_o_k': [0.116321, 0.093057], 'p_i': 10, 'u_i': 3.9687},
        {'id': 1, 'e_m': 0.250123, 'e_o_k': [0.069479, 0.055583], 'p_i': 20, 'u_i': 3.3202},
        {'id': 2, 'e_m': 5.305681, 'e_o_k': [1.473800, 1.179040], 'p_i': 40, 'u_i': 4.3833},
        {'id': 3, 'e_m': 3.803984, 'e_o_k': [1.056662, 0.845330], 'p_i': 80, 'u_i': 1.8853},
        {'id': 4, 'e_m': 1.413090, 'e_o_k': [0.392525, 0.314020], 'p_i': 20, 'u_i': 2.6679},
        {'id': 5, 'e_m': 0.064527, 'e_o_k': [0.017924, 0.014339], 'p_i': 10, 'u_i': 2.8390},
        {'id': 6, 'e_m': 0.594094, 'e_o_k': [0.165026, 0.132021], 'p_i': 40, 'u_i': 3.5794},
        {'id': 7, 'e_m': 2.938676, 'e_o_k': [0.816299, 0.653039], 'p_i': 40, 'u_i': 4.0478},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
