"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.744316, 'e_o_k': [0.155668, 0.124535, 0.099628, 0.079702, 0.063762], 'p_i': 10, 'u_i': 4.1058},
        {'id': 1, 'e_m': 1.039534, 'e_o_k': [0.127812, 0.102249, 0.081799], 'p_i': 20, 'u_i': 1.5782},
        {'id': 2, 'e_m': 3.119457, 'e_o_k': [0.278390, 0.222712, 0.178170, 0.142536, 0.114029], 'p_i': 40, 'u_i': 1.2072},
        {'id': 3, 'e_m': 8.153285, 'e_o_k': [0.727625, 0.582100, 0.465680, 0.372544, 0.298035], 'p_i': 80, 'u_i': 4.8515},
        {'id': 4, 'e_m': 1.529897, 'e_o_k': [0.124406, 0.099525, 0.079620, 0.063696, 0.050957, 0.040765], 'p_i': 20, 'u_i': 3.3809},
        {'id': 5, 'e_m': 32.069152, 'e_o_k': [3.259060, 2.607248, 2.085799, 1.668639], 'p_i': 80, 'u_i': 4.9290},
        {'id': 6, 'e_m': 2.718126, 'e_o_k': [0.453021, 0.362417], 'p_i': 20, 'u_i': 1.8035},
        {'id': 7, 'e_m': 3.804237, 'e_o_k': [0.386609, 0.309288, 0.247430, 0.197944], 'p_i': 10, 'u_i': 3.4846},
    ]
    B_BUDGET = 167.440003
    return processors, tasks, B_BUDGET
