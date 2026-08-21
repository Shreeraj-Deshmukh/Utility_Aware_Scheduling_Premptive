"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.187361, 'e_o_k': [0.052045, 0.041636], 'p_i': 10, 'u_i': 2.6135},
        {'id': 1, 'e_m': 2.315211, 'e_o_k': [0.313775, 0.251020, 0.200816, 0.160653, 0.128522, 0.102818], 'p_i': 20, 'u_i': 2.8871},
        {'id': 2, 'e_m': 6.099264, 'e_o_k': [0.826620, 0.661296, 0.529037, 0.423229, 0.338583, 0.270867], 'p_i': 40, 'u_i': 2.4127},
        {'id': 3, 'e_m': 15.366236, 'e_o_k': [3.148819, 2.519055, 2.015244], 'p_i': 80, 'u_i': 1.2331},
        {'id': 4, 'e_m': 6.272564, 'e_o_k': [1.285361, 1.028289, 0.822631], 'p_i': 40, 'u_i': 3.8857},
        {'id': 5, 'e_m': 3.282594, 'e_o_k': [0.911832, 0.729465], 'p_i': 20, 'u_i': 4.4773},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
