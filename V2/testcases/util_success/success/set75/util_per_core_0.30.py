"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759998, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759998, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.670330, 'e_o_k': [0.082418, 0.065934, 0.052747], 'p_i': 10, 'u_i': 4.1325},
        {'id': 1, 'e_m': 0.001538, 'e_o_k': [0.000156, 0.000125, 0.000100, 0.000080], 'p_i': 20, 'u_i': 2.4718},
        {'id': 2, 'e_m': 9.843899, 'e_o_k': [0.800473, 0.640379, 0.512303, 0.409842, 0.327874, 0.262299], 'p_i': 40, 'u_i': 1.1369},
        {'id': 3, 'e_m': 3.512611, 'e_o_k': [0.356973, 0.285578, 0.228462, 0.182770], 'p_i': 80, 'u_i': 2.0116},
        {'id': 4, 'e_m': 0.266517, 'e_o_k': [0.021672, 0.017338, 0.013870, 0.011096, 0.008877, 0.007102], 'p_i': 10, 'u_i': 3.8042},
        {'id': 5, 'e_m': 0.512779, 'e_o_k': [0.052112, 0.041689, 0.033351, 0.026681], 'p_i': 10, 'u_i': 3.9295},
        {'id': 6, 'e_m': 9.056965, 'e_o_k': [1.113561, 0.890849, 0.712679], 'p_i': 80, 'u_i': 2.7392},
        {'id': 7, 'e_m': 1.034867, 'e_o_k': [0.084152, 0.067322, 0.053857, 0.043086, 0.034469, 0.027575], 'p_i': 20, 'u_i': 3.4812},
    ]
    B_BUDGET = 71.759998
    return processors, tasks, B_BUDGET
