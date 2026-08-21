"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.383152, 'e_o_k': [0.159571, 0.127657, 0.102125, 0.081700, 0.065360], 'p_i': 10, 'u_i': 2.3860},
        {'id': 1, 'e_m': 0.611528, 'e_o_k': [0.475633, 0.380506], 'p_i': 20, 'u_i': 2.0962},
        {'id': 2, 'e_m': 2.560593, 'e_o_k': [1.214373, 0.971499, 0.777199, 0.621759], 'p_i': 40, 'u_i': 2.6459},
        {'id': 3, 'e_m': 2.908495, 'e_o_k': [1.103710, 0.882968, 0.706374, 0.565099, 0.452079, 0.361664], 'p_i': 80, 'u_i': 2.9249},
        {'id': 4, 'e_m': 8.125111, 'e_o_k': [3.083300, 2.466640, 1.973312, 1.578649, 1.262920, 1.010336], 'p_i': 80, 'u_i': 2.8041},
        {'id': 5, 'e_m': 5.166939, 'e_o_k': [4.018730, 3.214984], 'p_i': 40, 'u_i': 4.5045},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
