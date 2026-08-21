"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199994, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199994, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.554540, 'e_o_k': [0.191132, 0.152906, 0.122324], 'p_i': 10, 'u_i': 2.6742},
        {'id': 1, 'e_m': 0.707752, 'e_o_k': [0.057552, 0.046042, 0.036833, 0.029467, 0.023573, 0.018859], 'p_i': 20, 'u_i': 1.0126},
        {'id': 2, 'e_m': 1.636917, 'e_o_k': [0.146084, 0.116867, 0.093494, 0.074795, 0.059836], 'p_i': 40, 'u_i': 1.6645},
        {'id': 3, 'e_m': 36.483912, 'e_o_k': [3.255942, 2.604753, 2.083803, 1.667042, 1.333634], 'p_i': 80, 'u_i': 1.3774},
        {'id': 4, 'e_m': 9.208212, 'e_o_k': [1.534702, 1.227762], 'p_i': 40, 'u_i': 1.9412},
        {'id': 5, 'e_m': 2.142522, 'e_o_k': [0.357087, 0.285670], 'p_i': 10, 'u_i': 2.2237},
        {'id': 6, 'e_m': 4.763050, 'e_o_k': [0.585621, 0.468497, 0.374797], 'p_i': 10, 'u_i': 2.4269},
        {'id': 7, 'e_m': 31.313916, 'e_o_k': [3.182309, 2.545847, 2.036677, 1.629342], 'p_i': 80, 'u_i': 4.8879},
    ]
    B_BUDGET = 239.199994
    return processors, tasks, B_BUDGET
