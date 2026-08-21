"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.43999, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.43999, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.885126, 'e_o_k': [0.147521, 0.118017], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.341633, 'e_o_k': [0.042004, 0.033603, 0.026883], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 17.822399, 'e_o_k': [2.970400, 2.376320], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 11.482062, 'e_o_k': [0.933683, 0.746947, 0.597557, 0.478046, 0.382437, 0.305949], 'p_i': 80, 'u_i': 3.6242},
        {'id': 4, 'e_m': 7.943954, 'e_o_k': [1.323992, 1.059194], 'p_i': 20, 'u_i': 2.1240},
        {'id': 5, 'e_m': 11.839609, 'e_o_k': [1.203212, 0.962570, 0.770056, 0.616045], 'p_i': 80, 'u_i': 2.2796},
        {'id': 6, 'e_m': 1.898100, 'e_o_k': [0.169393, 0.135514, 0.108411, 0.086729, 0.069383], 'p_i': 20, 'u_i': 4.8637},
        {'id': 7, 'e_m': 0.652221, 'e_o_k': [0.080191, 0.064153, 0.051322], 'p_i': 10, 'u_i': 2.9768},
    ]
    B_BUDGET = 167.439990
    return processors, tasks, B_BUDGET
