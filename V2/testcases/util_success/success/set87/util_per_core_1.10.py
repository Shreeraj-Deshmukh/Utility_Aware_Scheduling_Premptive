"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119984, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119984, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.521157, 'e_o_k': [0.403483, 0.322786, 0.258229, 0.206583, 0.165266], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.872335, 'e_o_k': [0.107254, 0.085803, 0.068643], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 3.215891, 'e_o_k': [0.286996, 0.229597, 0.183678, 0.146942, 0.117554], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 33.835739, 'e_o_k': [4.160132, 3.328105, 2.662484], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 6.648659, 'e_o_k': [0.675677, 0.540541, 0.432433, 0.345947], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 4.844904, 'e_o_k': [0.807484, 0.645987], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 2.851096, 'e_o_k': [0.254441, 0.203553, 0.162842, 0.130274, 0.104219], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 6.254454, 'e_o_k': [0.558168, 0.446534, 0.357227, 0.285782, 0.228625], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 263.119984
    return processors, tasks, B_BUDGET
