"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.066228, 'e_o_k': [0.307328, 0.245862, 0.196690, 0.157352, 0.125882], 'p_i': 10, 'u_i': 1.1882},
        {'id': 1, 'e_m': 1.917825, 'e_o_k': [0.285255, 0.228204, 0.182563, 0.146050, 0.116840], 'p_i': 20, 'u_i': 4.0368},
        {'id': 2, 'e_m': 3.414456, 'e_o_k': [0.948460, 0.758768], 'p_i': 40, 'u_i': 1.1650},
        {'id': 3, 'e_m': 0.969960, 'e_o_k': [0.164289, 0.131431, 0.105145, 0.084116], 'p_i': 80, 'u_i': 2.0635},
    ]
    B_BUDGET = 55.199992
    return processors, tasks, B_BUDGET
