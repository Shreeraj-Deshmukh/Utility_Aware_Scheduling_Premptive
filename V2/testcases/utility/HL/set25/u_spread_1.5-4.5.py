"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 31, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 31, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.599440, 'e_o_k': [0.444289, 0.355431], 'p_i': 10, 'u_i': 2.5156},
        {'id': 1, 'e_m': 5.185523, 'e_o_k': [1.062607, 0.850086, 0.680069], 'p_i': 20, 'u_i': 4.1968},
        {'id': 2, 'e_m': 2.922224, 'e_o_k': [0.494957, 0.395965, 0.316772, 0.253418], 'p_i': 40, 'u_i': 3.7532},
        {'id': 3, 'e_m': 7.584490, 'e_o_k': [2.106803, 1.685442], 'p_i': 80, 'u_i': 1.8396},
        {'id': 4, 'e_m': 1.038987, 'e_o_k': [0.140812, 0.112649, 0.090119, 0.072096, 0.057676, 0.046141], 'p_i': 40, 'u_i': 4.4685},
        {'id': 5, 'e_m': 1.421690, 'e_o_k': [0.192679, 0.154143, 0.123314, 0.098651, 0.078921, 0.063137], 'p_i': 20, 'u_i': 2.3099},
        {'id': 6, 'e_m': 3.169787, 'e_o_k': [0.880496, 0.704397], 'p_i': 40, 'u_i': 1.6849},
        {'id': 7, 'e_m': 0.366143, 'e_o_k': [0.075029, 0.060023, 0.048019], 'p_i': 10, 'u_i': 3.5478},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
