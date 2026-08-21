"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759992, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759992, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.082511, 'e_o_k': [0.096607, 0.077285, 0.061828, 0.049463, 0.039570], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 3.744208, 'e_o_k': [0.624035, 0.499228], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 1.329751, 'e_o_k': [0.163494, 0.130795, 0.104636], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 3.615691, 'e_o_k': [0.367448, 0.293959, 0.235167, 0.188134], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 4.422543, 'e_o_k': [0.394682, 0.315746, 0.252596, 0.202077, 0.161662], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 6.895331, 'e_o_k': [1.149222, 0.919377], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.007139, 'e_o_k': [0.000726, 0.000580, 0.000464, 0.000371], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 0.583297, 'e_o_k': [0.071717, 0.057373, 0.045899], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 71.759992
    return processors, tasks, B_BUDGET
