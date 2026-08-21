"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 24, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 24, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.443349, 'e_o_k': [0.214682, 0.171745, 0.137396, 0.109917, 0.087934], 'p_i': 10, 'u_i': 3.4325},
        {'id': 1, 'e_m': 4.992277, 'e_o_k': [1.386744, 1.109395], 'p_i': 20, 'u_i': 2.7085},
        {'id': 2, 'e_m': 1.773001, 'e_o_k': [0.363320, 0.290656, 0.232525], 'p_i': 40, 'u_i': 2.7857},
        {'id': 3, 'e_m': 4.820922, 'e_o_k': [0.816552, 0.653241, 0.522593, 0.418075], 'p_i': 80, 'u_i': 3.1834},
        {'id': 4, 'e_m': 5.896724, 'e_o_k': [0.877071, 0.701657, 0.561325, 0.449060, 0.359248], 'p_i': 40, 'u_i': 3.1028},
        {'id': 5, 'e_m': 9.193774, 'e_o_k': [2.553826, 2.043061], 'p_i': 80, 'u_i': 2.9295},
        {'id': 6, 'e_m': 0.009519, 'e_o_k': [0.001612, 0.001290, 0.001032, 0.000825], 'p_i': 40, 'u_i': 2.9225},
        {'id': 7, 'e_m': 0.777730, 'e_o_k': [0.159371, 0.127497, 0.101997], 'p_i': 20, 'u_i': 3.3922},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
