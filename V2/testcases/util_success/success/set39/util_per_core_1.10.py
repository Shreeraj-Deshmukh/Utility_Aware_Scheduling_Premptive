"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.12001, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.12001, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.014617, 'e_o_k': [0.103112, 0.082489, 0.065991, 0.052793], 'p_i': 10, 'u_i': 1.8560},
        {'id': 1, 'e_m': 5.682272, 'e_o_k': [0.577467, 0.461973, 0.369579, 0.295663], 'p_i': 20, 'u_i': 4.8931},
        {'id': 2, 'e_m': 6.184853, 'e_o_k': [0.502932, 0.402345, 0.321876, 0.257501, 0.206001, 0.164801], 'p_i': 40, 'u_i': 4.2781},
        {'id': 3, 'e_m': 13.109005, 'e_o_k': [1.169890, 0.935912, 0.748729, 0.598984, 0.479187], 'p_i': 80, 'u_i': 3.3786},
        {'id': 4, 'e_m': 25.439991, 'e_o_k': [2.068696, 1.654956, 1.323965, 1.059172, 0.847338, 0.677870], 'p_i': 80, 'u_i': 4.8025},
        {'id': 5, 'e_m': 4.909036, 'e_o_k': [0.818173, 0.654538], 'p_i': 10, 'u_i': 2.8288},
        {'id': 6, 'e_m': 4.167835, 'e_o_k': [0.512439, 0.409951, 0.327961], 'p_i': 10, 'u_i': 2.6721},
        {'id': 7, 'e_m': 5.405077, 'e_o_k': [0.549296, 0.439437, 0.351550, 0.281240], 'p_i': 20, 'u_i': 4.7033},
    ]
    B_BUDGET = 263.120010
    return processors, tasks, B_BUDGET
