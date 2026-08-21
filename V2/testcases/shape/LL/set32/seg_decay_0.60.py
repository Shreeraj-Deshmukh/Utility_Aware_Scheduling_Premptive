"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200012, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.200012, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.507641, 'e_o_k': [0.110089, 0.066053, 0.039632, 0.023779, 0.014268], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 0.669069, 'e_o_k': [0.140362, 0.084217, 0.050530, 0.030318, 0.018191, 0.010915], 'p_i': 20, 'u_i': 2.4707},
        {'id': 2, 'e_m': 0.607685, 'e_o_k': [0.127485, 0.076491, 0.045895, 0.027537, 0.016522, 0.009913], 'p_i': 40, 'u_i': 1.1046},
        {'id': 3, 'e_m': 5.713737, 'e_o_k': [1.785543, 1.071326], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 2.096375, 'e_o_k': [0.481704, 0.289022, 0.173413, 0.104048], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.270524, 'e_o_k': [0.062161, 0.037297, 0.022378, 0.013427], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 2.830351, 'e_o_k': [0.884485, 0.530691], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.327572, 'e_o_k': [0.102366, 0.061420], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 55.200012
    return processors, tasks, B_BUDGET
