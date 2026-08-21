"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439997, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439997, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.007279, 'e_o_k': [0.334546, 0.267637], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 6.604072, 'e_o_k': [1.100679, 0.880543], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 9.363336, 'e_o_k': [1.151230, 0.920984, 0.736787], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 29.696182, 'e_o_k': [2.650183, 2.120146, 1.696117, 1.356894, 1.085515], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 1.924119, 'e_o_k': [0.236572, 0.189258, 0.151406], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.260687, 'e_o_k': [0.023265, 0.018612, 0.014889, 0.011911, 0.009529], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 5.771345, 'e_o_k': [0.469307, 0.375445, 0.300356, 0.240285, 0.192228, 0.153782], 'p_i': 80, 'u_i': 4.6383},
        {'id': 7, 'e_m': 6.592057, 'e_o_k': [0.588296, 0.470637, 0.376510, 0.301208, 0.240966], 'p_i': 80, 'u_i': 3.5515},
    ]
    B_BUDGET = 167.439997
    return processors, tasks, B_BUDGET
