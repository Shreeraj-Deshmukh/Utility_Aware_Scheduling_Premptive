"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679992, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679992, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.711602, 'e_o_k': [0.118600, 0.094880], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 1.956038, 'e_o_k': [0.159059, 0.127247, 0.101797, 0.081438, 0.065150, 0.052120], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 6.578908, 'e_o_k': [0.808882, 0.647106, 0.517685], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 14.898312, 'e_o_k': [1.831760, 1.465408, 1.172326], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 4.819102, 'e_o_k': [0.489746, 0.391797, 0.313438, 0.250750], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 0.459436, 'e_o_k': [0.037360, 0.029888, 0.023910, 0.019128, 0.015303, 0.012242], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 1.319662, 'e_o_k': [0.117771, 0.094217, 0.075373, 0.060299, 0.048239], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 2.163416, 'e_o_k': [0.360569, 0.288455], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 95.679992
    return processors, tasks, B_BUDGET
