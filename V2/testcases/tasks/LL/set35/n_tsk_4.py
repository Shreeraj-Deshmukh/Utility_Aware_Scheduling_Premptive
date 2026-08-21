"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.348629, 'e_o_k': [0.059050, 0.047240, 0.037792, 0.030233], 'p_i': 10, 'u_i': 1.6266},
        {'id': 1, 'e_m': 0.414411, 'e_o_k': [0.115114, 0.092091], 'p_i': 20, 'u_i': 2.5167},
        {'id': 2, 'e_m': 7.679884, 'e_o_k': [1.040838, 0.832670, 0.666136, 0.532909, 0.426327, 0.341062], 'p_i': 40, 'u_i': 3.7793},
        {'id': 3, 'e_m': 12.193553, 'e_o_k': [2.065304, 1.652243, 1.321794, 1.057436], 'p_i': 80, 'u_i': 1.9533},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
