"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320011, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320011, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.457470, 'e_o_k': [0.606990, 0.485592, 0.388474, 0.310779, 0.248623], 'p_i': 10, 'u_i': 3.3568},
        {'id': 1, 'e_m': 1.318732, 'e_o_k': [0.625415, 0.500332, 0.400265, 0.320212], 'p_i': 20, 'u_i': 2.9125},
        {'id': 2, 'e_m': 0.168487, 'e_o_k': [0.063937, 0.051150, 0.040920, 0.032736, 0.026189, 0.020951], 'p_i': 40, 'u_i': 4.1129},
        {'id': 3, 'e_m': 4.454265, 'e_o_k': [1.690295, 1.352236, 1.081789, 0.865431, 0.692345, 0.553876], 'p_i': 80, 'u_i': 4.6267},
        {'id': 4, 'e_m': 2.890958, 'e_o_k': [2.248523, 1.798818], 'p_i': 80, 'u_i': 4.4310},
        {'id': 5, 'e_m': 3.691560, 'e_o_k': [1.537418, 1.229934, 0.983947, 0.787158, 0.629726], 'p_i': 40, 'u_i': 4.5357},
    ]
    B_BUDGET = 88.320011
    return processors, tasks, B_BUDGET
