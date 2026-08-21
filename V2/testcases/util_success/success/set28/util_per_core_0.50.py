"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599999, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599999, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.042796, 'e_o_k': [0.173799, 0.139039], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 2.578686, 'e_o_k': [0.317052, 0.253641, 0.202913], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 2.711598, 'e_o_k': [0.451933, 0.361546], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 16.283732, 'e_o_k': [1.654851, 1.323881, 1.059105, 0.847284], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.351883, 'e_o_k': [0.058647, 0.046918], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 1.514647, 'e_o_k': [0.153928, 0.123142, 0.098514, 0.078811], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 1.481184, 'e_o_k': [0.182113, 0.145690, 0.116552], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 1.782722, 'e_o_k': [0.219187, 0.175350, 0.140280], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 119.599999
    return processors, tasks, B_BUDGET
