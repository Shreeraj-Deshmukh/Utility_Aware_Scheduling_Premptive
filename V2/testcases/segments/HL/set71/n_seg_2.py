"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.149966, 'e_o_k': [0.597213, 0.477770], 'p_i': 10, 'u_i': 1.0606},
        {'id': 1, 'e_m': 0.415795, 'e_o_k': [0.115499, 0.092399], 'p_i': 20, 'u_i': 3.4010},
        {'id': 2, 'e_m': 1.011654, 'e_o_k': [0.281015, 0.224812], 'p_i': 40, 'u_i': 1.6455},
        {'id': 3, 'e_m': 23.962531, 'e_o_k': [6.656259, 5.325007], 'p_i': 80, 'u_i': 1.3745},
        {'id': 4, 'e_m': 1.255643, 'e_o_k': [0.348790, 0.279032], 'p_i': 40, 'u_i': 1.5038},
        {'id': 5, 'e_m': 6.392981, 'e_o_k': [1.775828, 1.420662], 'p_i': 40, 'u_i': 4.4242},
        {'id': 6, 'e_m': 1.712311, 'e_o_k': [0.475642, 0.380514], 'p_i': 40, 'u_i': 1.3856},
        {'id': 7, 'e_m': 0.107345, 'e_o_k': [0.029818, 0.023854], 'p_i': 20, 'u_i': 2.4453},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
