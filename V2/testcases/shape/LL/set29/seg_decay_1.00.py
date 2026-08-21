"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199991, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.199991, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.277588, 'e_o_k': [0.034698, 0.034698, 0.034698, 0.034698], 'p_i': 10, 'u_i': 2.4751},
        {'id': 1, 'e_m': 0.425730, 'e_o_k': [0.042573, 0.042573, 0.042573, 0.042573, 0.042573], 'p_i': 20, 'u_i': 3.6644},
        {'id': 2, 'e_m': 1.697852, 'e_o_k': [0.169785, 0.169785, 0.169785, 0.169785, 0.169785], 'p_i': 40, 'u_i': 2.2976},
        {'id': 3, 'e_m': 1.741157, 'e_o_k': [0.174116, 0.174116, 0.174116, 0.174116, 0.174116], 'p_i': 80, 'u_i': 4.8639},
        {'id': 4, 'e_m': 2.016691, 'e_o_k': [0.504173, 0.504173], 'p_i': 40, 'u_i': 4.5045},
        {'id': 5, 'e_m': 1.394673, 'e_o_k': [0.232446, 0.232446, 0.232446], 'p_i': 80, 'u_i': 1.0020},
        {'id': 6, 'e_m': 1.783638, 'e_o_k': [0.222955, 0.222955, 0.222955, 0.222955], 'p_i': 40, 'u_i': 4.9529},
        {'id': 7, 'e_m': 1.743023, 'e_o_k': [0.435756, 0.435756], 'p_i': 10, 'u_i': 2.3587},
    ]
    B_BUDGET = 55.199991
    return processors, tasks, B_BUDGET
