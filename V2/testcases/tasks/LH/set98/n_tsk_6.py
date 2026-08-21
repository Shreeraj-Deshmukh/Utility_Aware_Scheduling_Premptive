"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319992, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319992, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.172281, 'e_o_k': [0.911774, 0.729420], 'p_i': 10, 'u_i': 3.5492},
        {'id': 1, 'e_m': 0.828834, 'e_o_k': [0.644649, 0.515719], 'p_i': 20, 'u_i': 2.1494},
        {'id': 2, 'e_m': 3.164984, 'e_o_k': [1.201041, 0.960833, 0.768666, 0.614933, 0.491946, 0.393557], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 0.143966, 'e_o_k': [0.111973, 0.089579], 'p_i': 80, 'u_i': 2.3334},
        {'id': 4, 'e_m': 0.630351, 'e_o_k': [0.361677, 0.289342, 0.231473], 'p_i': 80, 'u_i': 2.9112},
        {'id': 5, 'e_m': 3.050532, 'e_o_k': [1.270450, 1.016360, 0.813088, 0.650470, 0.520376], 'p_i': 20, 'u_i': 2.1467},
    ]
    B_BUDGET = 88.319992
    return processors, tasks, B_BUDGET
