"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.12, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.12, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.829738, 'e_o_k': [0.224968, 0.179974, 0.143979], 'p_i': 10, 'u_i': 2.5389},
        {'id': 1, 'e_m': 9.985651, 'e_o_k': [0.891152, 0.712921, 0.570337, 0.456270, 0.365016], 'p_i': 20, 'u_i': 1.9815},
        {'id': 2, 'e_m': 9.196230, 'e_o_k': [0.820701, 0.656561, 0.525249, 0.420199, 0.336159], 'p_i': 40, 'u_i': 1.2977},
        {'id': 3, 'e_m': 6.960933, 'e_o_k': [0.855852, 0.684682, 0.547746], 'p_i': 80, 'u_i': 4.3455},
        {'id': 4, 'e_m': 7.919719, 'e_o_k': [0.644005, 0.515204, 0.412163, 0.329731, 0.263785, 0.211028], 'p_i': 20, 'u_i': 2.7600},
        {'id': 5, 'e_m': 18.144826, 'e_o_k': [1.843986, 1.475189, 1.180151, 0.944121], 'p_i': 80, 'u_i': 1.5617},
        {'id': 6, 'e_m': 13.177437, 'e_o_k': [1.339170, 1.071336, 0.857069, 0.685655], 'p_i': 40, 'u_i': 2.1574},
        {'id': 7, 'e_m': 9.943762, 'e_o_k': [1.657294, 1.325835], 'p_i': 40, 'u_i': 1.2904},
    ]
    B_BUDGET = 263.120000
    return processors, tasks, B_BUDGET
