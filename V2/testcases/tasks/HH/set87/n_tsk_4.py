"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.323008, 'e_o_k': [1.575952, 1.260762, 1.008609, 0.806888], 'p_i': 10, 'u_i': 4.1671},
        {'id': 1, 'e_m': 0.682930, 'e_o_k': [0.391845, 0.313476, 0.250781], 'p_i': 20, 'u_i': 4.3098},
        {'id': 2, 'e_m': 3.722341, 'e_o_k': [1.765338, 1.412270, 1.129816, 0.903853], 'p_i': 40, 'u_i': 1.7953},
        {'id': 3, 'e_m': 27.239535, 'e_o_k': [10.336800, 8.269440, 6.615552, 5.292442, 4.233953, 3.387163], 'p_i': 80, 'u_i': 2.0773},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
