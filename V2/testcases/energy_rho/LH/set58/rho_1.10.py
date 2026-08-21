"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 93.472012, "H": 80, "J": 40, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.1, "seed": 1058, "set": 58, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.10"}
"""

_SPEC = '{"B": 93.472012, "H": 80, "J": 40, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.1, "seed": 1058, "set": 58, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.629540, 'e_o_k': [0.238897, 0.191117, 0.152894, 0.122315, 0.097852, 0.078282], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 1.955326, 'e_o_k': [1.520809, 1.216647], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.277667, 'e_o_k': [0.159317, 0.127454, 0.101963], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 2.558681, 'e_o_k': [1.990085, 1.592068], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 0.415486, 'e_o_k': [0.197046, 0.157637, 0.126110, 0.100888], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 6.998742, 'e_o_k': [5.443466, 4.354773], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 0.663543, 'e_o_k': [0.314688, 0.251751, 0.201401, 0.161120], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.049673, 'e_o_k': [0.023558, 0.018846, 0.015077, 0.012062], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 93.472012
    return processors, tasks, B_BUDGET
