"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 78.016001, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.8, "seed": 1076, "set": 76, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.80"}
"""

_SPEC = '{"B": 78.016001, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.8, "seed": 1076, "set": 76, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.547418, 'e_o_k': [0.259615, 0.207692, 0.166154, 0.132923], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 3.007680, 'e_o_k': [1.725718, 1.380575, 1.104460], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 0.682430, 'e_o_k': [0.258967, 0.207174, 0.165739, 0.132591, 0.106073, 0.084858], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 0.604649, 'e_o_k': [0.346930, 0.277544, 0.222035], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 1.249104, 'e_o_k': [0.592394, 0.473915, 0.379132, 0.303306], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 0.444853, 'e_o_k': [0.255243, 0.204195, 0.163356], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.188448, 'e_o_k': [0.146570, 0.117256], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 2.668510, 'e_o_k': [2.075507, 1.660406], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 78.016001
    return processors, tasks, B_BUDGET
