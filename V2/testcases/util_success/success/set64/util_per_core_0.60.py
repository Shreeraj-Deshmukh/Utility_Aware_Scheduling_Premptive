"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.52, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.52, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.165023, 'e_o_k': [0.193214, 0.154571, 0.123657, 0.098925, 0.079140], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 7.488416, 'e_o_k': [1.248069, 0.998455], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 2.659502, 'e_o_k': [0.326988, 0.261590, 0.209272], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 7.231383, 'e_o_k': [0.734897, 0.587917, 0.470334, 0.376267], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 8.845086, 'e_o_k': [0.789364, 0.631491, 0.505193, 0.404154, 0.323323], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 13.790661, 'e_o_k': [2.298444, 1.838755], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.014278, 'e_o_k': [0.001451, 0.001161, 0.000929, 0.000743], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 1.166594, 'e_o_k': [0.143434, 0.114747, 0.091798], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 143.520000
    return processors, tasks, B_BUDGET
