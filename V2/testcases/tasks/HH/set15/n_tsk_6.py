"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.914939, 'e_o_k': [1.213980, 0.971184, 0.776947, 0.621558, 0.497246], 'p_i': 10, 'u_i': 3.3568},
        {'id': 1, 'e_m': 2.637463, 'e_o_k': [1.250829, 1.000663, 0.800531, 0.640425], 'p_i': 20, 'u_i': 2.9125},
        {'id': 2, 'e_m': 0.336975, 'e_o_k': [0.127874, 0.102300, 0.081840, 0.065472, 0.052377, 0.041902], 'p_i': 40, 'u_i': 4.1129},
        {'id': 3, 'e_m': 8.908530, 'e_o_k': [3.380590, 2.704472, 2.163577, 1.730862, 1.384690, 1.107752], 'p_i': 80, 'u_i': 4.6267},
        {'id': 4, 'e_m': 5.781916, 'e_o_k': [4.497046, 3.597636], 'p_i': 80, 'u_i': 4.4310},
        {'id': 5, 'e_m': 7.383119, 'e_o_k': [3.074836, 2.459868, 1.967895, 1.574316, 1.259453], 'p_i': 40, 'u_i': 4.5357},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
