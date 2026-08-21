"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200008, "H": 80, "J": 21, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_split", "util_per_core": 0.2, "value": "LL"}
"""

_SPEC = '{"B": 55.200008, "H": 80, "J": 21, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_split", "util_per_core": 0.2, "value": "LL"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.333816, 'e_o_k': [0.056541, 0.045233, 0.036186, 0.028949], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 0.511403, 'e_o_k': [0.086620, 0.069296, 0.055437, 0.044349], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 2.476328, 'e_o_k': [0.687869, 0.550295], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 3.763800, 'e_o_k': [0.771271, 0.617016, 0.493613], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.262962, 'e_o_k': [0.053886, 0.043108, 0.034487], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 7.850730, 'e_o_k': [2.180758, 1.744607], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 3.101814, 'e_o_k': [0.861615, 0.689292], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 3.987120, 'e_o_k': [1.107533, 0.886027], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 55.200008
    return processors, tasks, B_BUDGET
