"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.122966, 'e_o_k': [0.172633, 0.138106, 0.110485, 0.088388, 0.070710, 0.056568], 'p_i': 10, 'u_i': 3.0798},
        {'id': 1, 'e_m': 8.994346, 'e_o_k': [1.105862, 0.884690, 0.707752], 'p_i': 20, 'u_i': 3.4237},
        {'id': 2, 'e_m': 0.180943, 'e_o_k': [0.014714, 0.011771, 0.009417, 0.007533, 0.006027, 0.004821], 'p_i': 40, 'u_i': 3.1726},
        {'id': 3, 'e_m': 22.094837, 'e_o_k': [3.682473, 2.945978], 'p_i': 80, 'u_i': 1.7653},
        {'id': 4, 'e_m': 17.222941, 'e_o_k': [1.400512, 1.120410, 0.896328, 0.717062, 0.573650, 0.458920], 'p_i': 80, 'u_i': 1.3860},
        {'id': 5, 'e_m': 1.180035, 'e_o_k': [0.095957, 0.076765, 0.061412, 0.049130, 0.039304, 0.031443], 'p_i': 10, 'u_i': 2.3150},
        {'id': 6, 'e_m': 2.342565, 'e_o_k': [0.390427, 0.312342], 'p_i': 10, 'u_i': 2.3741},
        {'id': 7, 'e_m': 3.589212, 'e_o_k': [0.320313, 0.256250, 0.205000, 0.164000, 0.131200], 'p_i': 40, 'u_i': 4.2099},
    ]
    B_BUDGET = 191.360001
    return processors, tasks, B_BUDGET
