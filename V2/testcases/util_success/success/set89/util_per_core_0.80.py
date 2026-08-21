"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360017, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360017, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.216025, 'e_o_k': [0.518364, 0.414691, 0.331753], 'p_i': 10, 'u_i': 2.9983},
        {'id': 1, 'e_m': 3.965910, 'e_o_k': [0.660985, 0.528788], 'p_i': 20, 'u_i': 1.1603},
        {'id': 2, 'e_m': 1.140846, 'e_o_k': [0.115940, 0.092752, 0.074201, 0.059361], 'p_i': 40, 'u_i': 4.9504},
        {'id': 3, 'e_m': 2.844534, 'e_o_k': [0.349738, 0.279790, 0.223832], 'p_i': 80, 'u_i': 4.4756},
        {'id': 4, 'e_m': 7.900678, 'e_o_k': [0.971395, 0.777116, 0.621693], 'p_i': 20, 'u_i': 1.0040},
        {'id': 5, 'e_m': 4.945327, 'e_o_k': [0.824221, 0.659377], 'p_i': 10, 'u_i': 3.8708},
        {'id': 6, 'e_m': 0.058423, 'e_o_k': [0.005214, 0.004171, 0.003337, 0.002670, 0.002136], 'p_i': 10, 'u_i': 4.3902},
        {'id': 7, 'e_m': 1.649222, 'e_o_k': [0.202773, 0.162219, 0.129775], 'p_i': 80, 'u_i': 4.5183},
    ]
    B_BUDGET = 191.360017
    return processors, tasks, B_BUDGET
