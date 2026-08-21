"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.811128, 'e_o_k': [0.503091, 0.402473], 'p_i': 10, 'u_i': 3.4311},
        {'id': 1, 'e_m': 0.050717, 'e_o_k': [0.014088, 0.011270], 'p_i': 20, 'u_i': 3.8774},
        {'id': 2, 'e_m': 2.544213, 'e_o_k': [0.706726, 0.565381], 'p_i': 40, 'u_i': 3.3220},
        {'id': 3, 'e_m': 1.179546, 'e_o_k': [0.327652, 0.262121], 'p_i': 80, 'u_i': 2.5309},
        {'id': 4, 'e_m': 1.744117, 'e_o_k': [0.484477, 0.387582], 'p_i': 40, 'u_i': 3.7128},
        {'id': 5, 'e_m': 0.579467, 'e_o_k': [0.160963, 0.128770], 'p_i': 20, 'u_i': 4.9574},
        {'id': 6, 'e_m': 4.549467, 'e_o_k': [1.263741, 1.010993], 'p_i': 80, 'u_i': 3.9330},
        {'id': 7, 'e_m': 0.342286, 'e_o_k': [0.095079, 0.076064], 'p_i': 40, 'u_i': 3.5882},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
