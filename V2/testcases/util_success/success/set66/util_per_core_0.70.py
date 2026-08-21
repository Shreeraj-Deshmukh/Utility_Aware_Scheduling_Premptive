"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439987, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439987, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.234993, 'e_o_k': [0.023881, 0.019105, 0.015284, 0.012227], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 2.791434, 'e_o_k': [0.249117, 0.199293, 0.159435, 0.127548, 0.102038], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 7.152246, 'e_o_k': [0.879374, 0.703500, 0.562800], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 17.696421, 'e_o_k': [2.175789, 1.740632, 1.392505], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 3.352929, 'e_o_k': [0.558822, 0.447057], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 1.759387, 'e_o_k': [0.293231, 0.234585], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 1.913622, 'e_o_k': [0.194474, 0.155579, 0.124463, 0.099571], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 37.552967, 'e_o_k': [4.617168, 3.693734, 2.954988], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 167.439987
    return processors, tasks, B_BUDGET
