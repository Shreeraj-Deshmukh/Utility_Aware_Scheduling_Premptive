"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 35, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 35, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.728311, 'e_o_k': [0.123359, 0.098687, 0.078950, 0.063160], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 3.236491, 'e_o_k': [0.663215, 0.530572, 0.424458], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 0.535015, 'e_o_k': [0.109634, 0.087707, 0.070166], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 4.750488, 'e_o_k': [0.643823, 0.515059, 0.412047, 0.329637, 0.263710, 0.210968], 'p_i': 80, 'u_i': 1.9048},
        {'id': 4, 'e_m': 0.182718, 'e_o_k': [0.050755, 0.040604], 'p_i': 40, 'u_i': 4.4078},
        {'id': 5, 'e_m': 0.092022, 'e_o_k': [0.018857, 0.015086, 0.012068], 'p_i': 10, 'u_i': 3.6020},
        {'id': 6, 'e_m': 2.641333, 'e_o_k': [0.447380, 0.357904, 0.286323, 0.229059], 'p_i': 40, 'u_i': 4.8789},
        {'id': 7, 'e_m': 0.127844, 'e_o_k': [0.021654, 0.017323, 0.013858, 0.011087], 'p_i': 10, 'u_i': 3.0372},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
