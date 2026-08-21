"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439989, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439989, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.459417, 'e_o_k': [0.046689, 0.037351, 0.029881, 0.023905], 'p_i': 10, 'u_i': 4.2383},
        {'id': 1, 'e_m': 4.988775, 'e_o_k': [0.445214, 0.356171, 0.284937, 0.227950, 0.182360], 'p_i': 20, 'u_i': 1.1754},
        {'id': 2, 'e_m': 7.843970, 'e_o_k': [1.307328, 1.045863], 'p_i': 40, 'u_i': 2.9766},
        {'id': 3, 'e_m': 19.496142, 'e_o_k': [1.585362, 1.268289, 1.014631, 0.811705, 0.649364, 0.519491], 'p_i': 80, 'u_i': 4.8798},
        {'id': 4, 'e_m': 20.816482, 'e_o_k': [1.692727, 1.354182, 1.083345, 0.866676, 0.693341, 0.554673], 'p_i': 80, 'u_i': 3.7063},
        {'id': 5, 'e_m': 2.740491, 'e_o_k': [0.244570, 0.195656, 0.156525, 0.125220, 0.100176], 'p_i': 10, 'u_i': 2.9881},
        {'id': 6, 'e_m': 0.906723, 'e_o_k': [0.080919, 0.064735, 0.051788, 0.041430, 0.033144], 'p_i': 20, 'u_i': 3.8057},
        {'id': 7, 'e_m': 6.818174, 'e_o_k': [1.136362, 0.909090], 'p_i': 80, 'u_i': 1.4079},
    ]
    B_BUDGET = 167.439989
    return processors, tasks, B_BUDGET
