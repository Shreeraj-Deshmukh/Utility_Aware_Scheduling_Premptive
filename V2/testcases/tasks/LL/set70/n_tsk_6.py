"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200011, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200011, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.762181, 'e_o_k': [0.211717, 0.169374], 'p_i': 10, 'u_i': 1.8882},
        {'id': 1, 'e_m': 2.928001, 'e_o_k': [0.435507, 0.348406, 0.278725, 0.222980, 0.178384], 'p_i': 20, 'u_i': 2.0463},
        {'id': 2, 'e_m': 5.383574, 'e_o_k': [0.800746, 0.640597, 0.512477, 0.409982, 0.327985], 'p_i': 40, 'u_i': 1.5718},
        {'id': 3, 'e_m': 1.416998, 'e_o_k': [0.393611, 0.314889], 'p_i': 80, 'u_i': 2.9208},
        {'id': 4, 'e_m': 0.074139, 'e_o_k': [0.010048, 0.008038, 0.006431, 0.005145, 0.004116, 0.003292], 'p_i': 20, 'u_i': 4.6964},
        {'id': 5, 'e_m': 1.709844, 'e_o_k': [0.350378, 0.280302, 0.224242], 'p_i': 80, 'u_i': 4.6519},
    ]
    B_BUDGET = 55.200011
    return processors, tasks, B_BUDGET
