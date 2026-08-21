"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199993, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199993, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.451663, 'e_o_k': [0.075277, 0.060222], 'p_i': 10, 'u_i': 1.3417},
        {'id': 1, 'e_m': 6.361236, 'e_o_k': [0.782119, 0.625695, 0.500556], 'p_i': 20, 'u_i': 1.8511},
        {'id': 2, 'e_m': 11.655304, 'e_o_k': [1.040157, 0.832125, 0.665700, 0.532560, 0.426048], 'p_i': 40, 'u_i': 4.0269},
        {'id': 3, 'e_m': 21.682229, 'e_o_k': [3.613705, 2.890964], 'p_i': 80, 'u_i': 1.9345},
        {'id': 4, 'e_m': 8.253210, 'e_o_k': [1.375535, 1.100428], 'p_i': 20, 'u_i': 3.7416},
        {'id': 5, 'e_m': 32.705926, 'e_o_k': [4.021220, 3.216976, 2.573581], 'p_i': 80, 'u_i': 1.3128},
        {'id': 6, 'e_m': 1.881039, 'e_o_k': [0.231275, 0.185020, 0.148016], 'p_i': 10, 'u_i': 1.5894},
        {'id': 7, 'e_m': 5.181841, 'e_o_k': [0.421370, 0.337096, 0.269677, 0.215741, 0.172593, 0.138075], 'p_i': 80, 'u_i': 3.8422},
    ]
    B_BUDGET = 239.199993
    return processors, tasks, B_BUDGET
