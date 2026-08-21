"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "shape", "util_per_core": 0.2, "value": "0.80"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "shape", "util_per_core": 0.2, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.050222, 'e_o_k': [0.028816, 0.023053, 0.018442], 'p_i': 10, 'u_i': 2.4144},
        {'id': 1, 'e_m': 0.206926, 'e_o_k': [0.160942, 0.128754], 'p_i': 20, 'u_i': 2.6559},
        {'id': 2, 'e_m': 1.190379, 'e_o_k': [0.495755, 0.396604, 0.317283, 0.253827, 0.203061], 'p_i': 40, 'u_i': 2.8681},
        {'id': 3, 'e_m': 6.971948, 'e_o_k': [5.422626, 4.338101], 'p_i': 80, 'u_i': 1.8896},
        {'id': 4, 'e_m': 0.550862, 'e_o_k': [0.229417, 0.183533, 0.146827, 0.117461, 0.093969], 'p_i': 20, 'u_i': 1.6645},
        {'id': 5, 'e_m': 0.291867, 'e_o_k': [0.121553, 0.097243, 0.077794, 0.062235, 0.049788], 'p_i': 40, 'u_i': 1.3774},
        {'id': 6, 'e_m': 1.611679, 'e_o_k': [1.253528, 1.002823], 'p_i': 80, 'u_i': 1.9412},
        {'id': 7, 'e_m': 17.018957, 'e_o_k': [13.236966, 10.589573], 'p_i': 80, 'u_i': 2.2237},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
