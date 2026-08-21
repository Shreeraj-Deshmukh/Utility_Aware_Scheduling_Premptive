"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759994, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759994, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.804907, 'e_o_k': [0.065452, 0.052362, 0.041890, 0.033512, 0.026809, 0.021447], 'p_i': 10, 'u_i': 3.0333},
        {'id': 1, 'e_m': 1.507367, 'e_o_k': [0.122574, 0.098059, 0.078447, 0.062758, 0.050206, 0.040165], 'p_i': 20, 'u_i': 1.6855},
        {'id': 2, 'e_m': 3.375317, 'e_o_k': [0.301224, 0.240979, 0.192783, 0.154227, 0.123381], 'p_i': 40, 'u_i': 1.7213},
        {'id': 3, 'e_m': 3.880593, 'e_o_k': [0.315557, 0.252446, 0.201956, 0.161565, 0.129252, 0.103402], 'p_i': 80, 'u_i': 2.0710},
        {'id': 4, 'e_m': 3.405911, 'e_o_k': [0.346129, 0.276903, 0.221523, 0.177218], 'p_i': 80, 'u_i': 2.4462},
        {'id': 5, 'e_m': 0.514298, 'e_o_k': [0.052266, 0.041813, 0.033450, 0.026760], 'p_i': 10, 'u_i': 2.4016},
        {'id': 6, 'e_m': 11.322086, 'e_o_k': [1.392060, 1.113648, 0.890918], 'p_i': 80, 'u_i': 3.4602},
        {'id': 7, 'e_m': 6.057672, 'e_o_k': [0.615617, 0.492494, 0.393995, 0.315196], 'p_i': 80, 'u_i': 3.9709},
    ]
    B_BUDGET = 71.759994
    return processors, tasks, B_BUDGET
