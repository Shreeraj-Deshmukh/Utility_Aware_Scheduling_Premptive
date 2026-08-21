"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120003, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120003, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.476926, 'e_o_k': [0.038782, 0.031026, 0.024821, 0.019856, 0.015885, 0.012708], 'p_i': 10, 'u_i': 3.1766},
        {'id': 1, 'e_m': 8.968510, 'e_o_k': [0.729289, 0.583432, 0.466745, 0.373396, 0.298717, 0.238974], 'p_i': 20, 'u_i': 1.6887},
        {'id': 2, 'e_m': 2.521381, 'e_o_k': [0.225016, 0.180013, 0.144010, 0.115208, 0.092167], 'p_i': 40, 'u_i': 3.5480},
        {'id': 3, 'e_m': 32.386197, 'e_o_k': [3.291280, 2.633024, 2.106419, 1.685135], 'p_i': 80, 'u_i': 3.7765},
        {'id': 4, 'e_m': 14.664305, 'e_o_k': [1.308690, 1.046952, 0.837561, 0.670049, 0.536039], 'p_i': 40, 'u_i': 3.9794},
        {'id': 5, 'e_m': 15.371123, 'e_o_k': [1.889892, 1.511914, 1.209531], 'p_i': 80, 'u_i': 3.8371},
        {'id': 6, 'e_m': 4.125964, 'e_o_k': [0.687661, 0.550129], 'p_i': 10, 'u_i': 4.0284},
        {'id': 7, 'e_m': 21.174147, 'e_o_k': [1.721811, 1.377449, 1.101959, 0.881567, 0.705254, 0.564203], 'p_i': 80, 'u_i': 4.5608},
    ]
    B_BUDGET = 263.120003
    return processors, tasks, B_BUDGET
