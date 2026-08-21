"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200003, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200003, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.815047, 'e_o_k': [0.592014, 0.473611, 0.378889], 'p_i': 10, 'u_i': 2.2709},
        {'id': 1, 'e_m': 6.160678, 'e_o_k': [1.026780, 0.821424], 'p_i': 20, 'u_i': 3.6947},
        {'id': 2, 'e_m': 7.298445, 'e_o_k': [1.216407, 0.973126], 'p_i': 40, 'u_i': 2.6358},
        {'id': 3, 'e_m': 0.467299, 'e_o_k': [0.041703, 0.033363, 0.026690, 0.021352, 0.017082], 'p_i': 80, 'u_i': 2.5174},
        {'id': 4, 'e_m': 18.775820, 'e_o_k': [1.526787, 1.221430, 0.977144, 0.781715, 0.625372, 0.500298], 'p_i': 80, 'u_i': 4.4047},
        {'id': 5, 'e_m': 24.369254, 'e_o_k': [1.981627, 1.585301, 1.268241, 1.014593, 0.811674, 0.649339], 'p_i': 80, 'u_i': 1.7061},
        {'id': 6, 'e_m': 13.307741, 'e_o_k': [1.352413, 1.081930, 0.865544, 0.692435], 'p_i': 80, 'u_i': 3.8123},
        {'id': 7, 'e_m': 6.329977, 'e_o_k': [0.564908, 0.451926, 0.361541, 0.289233, 0.231386], 'p_i': 20, 'u_i': 3.3653},
    ]
    B_BUDGET = 239.200003
    return processors, tasks, B_BUDGET
