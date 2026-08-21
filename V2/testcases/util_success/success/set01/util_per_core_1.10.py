"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119995, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119995, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.735883, 'e_o_k': [0.422645, 0.338116, 0.270493, 0.216394, 0.173116], 'p_i': 10, 'u_i': 2.0357},
        {'id': 1, 'e_m': 9.810488, 'e_o_k': [0.875520, 0.700416, 0.560332, 0.448266, 0.358613], 'p_i': 20, 'u_i': 4.7280},
        {'id': 2, 'e_m': 2.416178, 'e_o_k': [0.245547, 0.196437, 0.157150, 0.125720], 'p_i': 40, 'u_i': 3.3583},
        {'id': 3, 'e_m': 23.145037, 'e_o_k': [2.845701, 2.276561, 1.821249], 'p_i': 80, 'u_i': 2.7036},
        {'id': 4, 'e_m': 0.545738, 'e_o_k': [0.055461, 0.044369, 0.035495, 0.028396], 'p_i': 40, 'u_i': 1.9481},
        {'id': 5, 'e_m': 4.244156, 'e_o_k': [0.707359, 0.565887], 'p_i': 10, 'u_i': 1.0528},
        {'id': 6, 'e_m': 5.344946, 'e_o_k': [0.434633, 0.347707, 0.278165, 0.222532, 0.178026, 0.142421], 'p_i': 80, 'u_i': 1.9568},
        {'id': 7, 'e_m': 3.812991, 'e_o_k': [0.635498, 0.508399], 'p_i': 10, 'u_i': 4.3968},
    ]
    B_BUDGET = 263.119995
    return processors, tasks, B_BUDGET
