"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120003, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120003, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.721942, 'e_o_k': [0.073368, 0.058694, 0.046956, 0.037564], 'p_i': 10, 'u_i': 4.2383},
        {'id': 1, 'e_m': 7.839504, 'e_o_k': [0.699623, 0.559698, 0.447758, 0.358207, 0.286565], 'p_i': 20, 'u_i': 1.1754},
        {'id': 2, 'e_m': 12.326239, 'e_o_k': [2.054373, 1.643498], 'p_i': 40, 'u_i': 2.9766},
        {'id': 3, 'e_m': 30.636794, 'e_o_k': [2.491282, 1.993026, 1.594421, 1.275537, 1.020429, 0.816343], 'p_i': 80, 'u_i': 4.8798},
        {'id': 4, 'e_m': 32.711615, 'e_o_k': [2.660000, 2.128000, 1.702400, 1.361920, 1.089536, 0.871629], 'p_i': 80, 'u_i': 3.7063},
        {'id': 5, 'e_m': 4.306487, 'e_o_k': [0.384325, 0.307460, 0.245968, 0.196774, 0.157419], 'p_i': 10, 'u_i': 2.9881},
        {'id': 6, 'e_m': 1.424850, 'e_o_k': [0.127158, 0.101727, 0.081381, 0.065105, 0.052084], 'p_i': 20, 'u_i': 3.8057},
        {'id': 7, 'e_m': 10.714273, 'e_o_k': [1.785712, 1.428570], 'p_i': 80, 'u_i': 1.4079},
    ]
    B_BUDGET = 263.120003
    return processors, tasks, B_BUDGET
