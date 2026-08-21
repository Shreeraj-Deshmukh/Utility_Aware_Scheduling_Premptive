"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199994, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199994, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.774518, 'e_o_k': [0.629086, 0.503269], 'p_i': 10, 'u_i': 3.5122},
        {'id': 1, 'e_m': 4.850352, 'e_o_k': [0.394415, 0.315532, 0.252425, 0.201940, 0.161552, 0.129242], 'p_i': 20, 'u_i': 2.8569},
        {'id': 2, 'e_m': 9.832441, 'e_o_k': [1.638740, 1.310992], 'p_i': 40, 'u_i': 4.3008},
        {'id': 3, 'e_m': 5.018023, 'e_o_k': [0.509962, 0.407969, 0.326375, 0.261100], 'p_i': 80, 'u_i': 2.2362},
        {'id': 4, 'e_m': 4.848865, 'e_o_k': [0.492771, 0.394217, 0.315373, 0.252299], 'p_i': 10, 'u_i': 3.7312},
        {'id': 5, 'e_m': 1.046462, 'e_o_k': [0.106348, 0.085078, 0.068063, 0.054450], 'p_i': 20, 'u_i': 3.2074},
        {'id': 6, 'e_m': 14.053484, 'e_o_k': [1.254178, 1.003342, 0.802674, 0.642139, 0.513711], 'p_i': 80, 'u_i': 3.9809},
        {'id': 7, 'e_m': 28.689286, 'e_o_k': [4.781548, 3.825238], 'p_i': 80, 'u_i': 1.3445},
    ]
    B_BUDGET = 239.199994
    return processors, tasks, B_BUDGET
