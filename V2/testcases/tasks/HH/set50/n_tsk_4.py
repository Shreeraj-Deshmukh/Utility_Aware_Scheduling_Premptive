"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.516602, 'e_o_k': [1.193511, 0.954809, 0.763847, 0.611077], 'p_i': 10, 'u_i': 4.9008},
        {'id': 1, 'e_m': 2.398320, 'e_o_k': [1.865360, 1.492288], 'p_i': 20, 'u_i': 4.5033},
        {'id': 2, 'e_m': 9.438732, 'e_o_k': [5.415666, 4.332533, 3.466026], 'p_i': 40, 'u_i': 2.6753},
        {'id': 3, 'e_m': 15.396438, 'e_o_k': [11.975007, 9.580006], 'p_i': 80, 'u_i': 4.2784},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET
