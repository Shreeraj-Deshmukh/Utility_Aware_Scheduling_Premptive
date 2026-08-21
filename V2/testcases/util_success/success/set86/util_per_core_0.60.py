"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519983, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519983, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.932724, 'e_o_k': [0.114679, 0.091743, 0.073395], 'p_i': 10, 'u_i': 2.6742},
        {'id': 1, 'e_m': 0.424651, 'e_o_k': [0.034531, 0.027625, 0.022100, 0.017680, 0.014144, 0.011315], 'p_i': 20, 'u_i': 1.0126},
        {'id': 2, 'e_m': 0.982150, 'e_o_k': [0.087650, 0.070120, 0.056096, 0.044877, 0.035902], 'p_i': 40, 'u_i': 1.6645},
        {'id': 3, 'e_m': 21.890347, 'e_o_k': [1.953565, 1.562852, 1.250282, 1.000225, 0.800180], 'p_i': 80, 'u_i': 1.3774},
        {'id': 4, 'e_m': 5.524927, 'e_o_k': [0.920821, 0.736657], 'p_i': 40, 'u_i': 1.9412},
        {'id': 5, 'e_m': 1.285513, 'e_o_k': [0.214252, 0.171402], 'p_i': 10, 'u_i': 2.2237},
        {'id': 6, 'e_m': 2.857830, 'e_o_k': [0.351373, 0.281098, 0.224878], 'p_i': 10, 'u_i': 2.4269},
        {'id': 7, 'e_m': 18.788350, 'e_o_k': [1.909385, 1.527508, 1.222006, 0.977605], 'p_i': 80, 'u_i': 4.8879},
    ]
    B_BUDGET = 143.519983
    return processors, tasks, B_BUDGET
