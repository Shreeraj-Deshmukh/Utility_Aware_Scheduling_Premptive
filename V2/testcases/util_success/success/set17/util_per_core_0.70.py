"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.388670, 'e_o_k': [0.112922, 0.090338, 0.072270, 0.057816, 0.046253, 0.037002], 'p_i': 10, 'u_i': 2.9192},
        {'id': 1, 'e_m': 1.837375, 'e_o_k': [0.186725, 0.149380, 0.119504, 0.095603], 'p_i': 20, 'u_i': 2.0454},
        {'id': 2, 'e_m': 13.190774, 'e_o_k': [1.072630, 0.858104, 0.686483, 0.549187, 0.439349, 0.351479], 'p_i': 40, 'u_i': 2.8602},
        {'id': 3, 'e_m': 29.963720, 'e_o_k': [4.993953, 3.995163], 'p_i': 80, 'u_i': 2.9521},
        {'id': 4, 'e_m': 1.494624, 'e_o_k': [0.249104, 0.199283], 'p_i': 10, 'u_i': 3.5497},
        {'id': 5, 'e_m': 5.797109, 'e_o_k': [0.589137, 0.471310, 0.377048, 0.301638], 'p_i': 40, 'u_i': 2.7971},
        {'id': 6, 'e_m': 3.217877, 'e_o_k': [0.261667, 0.209334, 0.167467, 0.133974, 0.107179, 0.085743], 'p_i': 80, 'u_i': 4.6429},
        {'id': 7, 'e_m': 10.426786, 'e_o_k': [1.737798, 1.390238], 'p_i': 80, 'u_i': 1.6248},
    ]
    B_BUDGET = 167.439999
    return processors, tasks, B_BUDGET
