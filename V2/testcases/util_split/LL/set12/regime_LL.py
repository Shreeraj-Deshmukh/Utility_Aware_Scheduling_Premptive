"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 25, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_split", "util_per_core": 0.2, "value": "LL"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 25, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_split", "util_per_core": 0.2, "value": "LL"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.573508, 'e_o_k': [0.159308, 0.127446], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 1.886878, 'e_o_k': [0.524133, 0.419306], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 2.675239, 'e_o_k': [0.548205, 0.438564, 0.350851], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 8.484623, 'e_o_k': [1.261992, 1.009593, 0.807675, 0.646140, 0.516912], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 0.549748, 'e_o_k': [0.112653, 0.090123, 0.072098], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.074482, 'e_o_k': [0.011078, 0.008863, 0.007090, 0.005672, 0.004538], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 1.648956, 'e_o_k': [0.223479, 0.178783, 0.143027, 0.114421, 0.091537, 0.073230], 'p_i': 80, 'u_i': 4.6383},
        {'id': 7, 'e_m': 1.883445, 'e_o_k': [0.280141, 0.224113, 0.179290, 0.143432, 0.114746], 'p_i': 80, 'u_i': 3.5515},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
