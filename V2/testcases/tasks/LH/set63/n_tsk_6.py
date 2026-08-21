"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.103477, 'e_o_k': [0.459563, 0.367651, 0.294121, 0.235296, 0.188237], 'p_i': 10, 'u_i': 2.2919},
        {'id': 1, 'e_m': 0.023443, 'e_o_k': [0.008896, 0.007117, 0.005694, 0.004555, 0.003644, 0.002915], 'p_i': 20, 'u_i': 3.9772},
        {'id': 2, 'e_m': 2.133839, 'e_o_k': [1.011983, 0.809587, 0.647669, 0.518135], 'p_i': 40, 'u_i': 1.4627},
        {'id': 3, 'e_m': 1.363358, 'e_o_k': [1.060390, 0.848312], 'p_i': 80, 'u_i': 4.5040},
        {'id': 4, 'e_m': 1.081537, 'e_o_k': [0.620554, 0.496443, 0.397155], 'p_i': 20, 'u_i': 4.7123},
        {'id': 5, 'e_m': 6.560614, 'e_o_k': [2.732288, 2.185830, 1.748664, 1.398931, 1.119145], 'p_i': 40, 'u_i': 4.3702},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
