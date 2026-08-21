"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.766304, 'e_o_k': [0.113979, 0.091183, 0.072947, 0.058357, 0.046686], 'p_i': 10, 'u_i': 2.3860},
        {'id': 1, 'e_m': 1.223056, 'e_o_k': [0.339738, 0.271790], 'p_i': 20, 'u_i': 2.0962},
        {'id': 2, 'e_m': 5.121185, 'e_o_k': [0.867409, 0.693928, 0.555142, 0.444114], 'p_i': 40, 'u_i': 2.6459},
        {'id': 3, 'e_m': 5.816991, 'e_o_k': [0.788364, 0.630691, 0.504553, 0.403642, 0.322914, 0.258331], 'p_i': 80, 'u_i': 2.9249},
        {'id': 4, 'e_m': 16.250223, 'e_o_k': [2.202357, 1.761886, 1.409508, 1.127607, 0.902085, 0.721668], 'p_i': 80, 'u_i': 2.8041},
        {'id': 5, 'e_m': 10.333878, 'e_o_k': [2.870522, 2.296417], 'p_i': 40, 'u_i': 4.5045},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET
