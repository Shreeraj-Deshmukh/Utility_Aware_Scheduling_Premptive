"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.721674, 'e_o_k': [0.561302, 0.449042], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 2.496139, 'e_o_k': [1.941441, 1.553153], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 0.886501, 'e_o_k': [0.689500, 0.551600], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 2.410461, 'e_o_k': [1.874803, 1.499842], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 2.948362, 'e_o_k': [2.293171, 1.834536], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 4.596887, 'e_o_k': [3.575357, 2.860285], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.004759, 'e_o_k': [0.003702, 0.002961], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 0.388865, 'e_o_k': [0.302450, 0.241960], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
