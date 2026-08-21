"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200001, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200001, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.098466, 'e_o_k': [0.089324, 0.071459, 0.057167, 0.045734, 0.036587, 0.029270], 'p_i': 10, 'u_i': 3.3901},
        {'id': 1, 'e_m': 8.453053, 'e_o_k': [0.687374, 0.549899, 0.439919, 0.351936, 0.281548, 0.225239], 'p_i': 20, 'u_i': 2.3217},
        {'id': 2, 'e_m': 11.252767, 'e_o_k': [1.143574, 0.914859, 0.731887, 0.585510], 'p_i': 40, 'u_i': 2.1118},
        {'id': 3, 'e_m': 3.241681, 'e_o_k': [0.329439, 0.263551, 0.210841, 0.168673], 'p_i': 80, 'u_i': 4.2305},
        {'id': 4, 'e_m': 36.344850, 'e_o_k': [6.057475, 4.845980], 'p_i': 80, 'u_i': 2.0791},
        {'id': 5, 'e_m': 19.870539, 'e_o_k': [3.311757, 2.649405], 'p_i': 80, 'u_i': 1.4810},
        {'id': 6, 'e_m': 18.090296, 'e_o_k': [3.015049, 2.412039], 'p_i': 80, 'u_i': 3.5439},
        {'id': 7, 'e_m': 2.168395, 'e_o_k': [0.176327, 0.141061, 0.112849, 0.090279, 0.072223, 0.057779], 'p_i': 10, 'u_i': 4.1958},
    ]
    B_BUDGET = 239.200001
    return processors, tasks, B_BUDGET
