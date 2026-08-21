"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.735977, 'e_o_k': [0.306511, 0.245209, 0.196167, 0.156934, 0.125547], 'p_i': 10, 'u_i': 1.2401},
        {'id': 1, 'e_m': 1.272862, 'e_o_k': [0.530107, 0.424085, 0.339268, 0.271415, 0.217132], 'p_i': 20, 'u_i': 2.2762},
        {'id': 2, 'e_m': 6.649816, 'e_o_k': [2.769438, 2.215550, 1.772440, 1.417952, 1.134362], 'p_i': 40, 'u_i': 1.0661},
        {'id': 3, 'e_m': 7.721105, 'e_o_k': [3.661770, 2.929416, 2.343533, 1.874826], 'p_i': 80, 'u_i': 2.9903},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
