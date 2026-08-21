"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.134282, 'e_o_k': [0.030855, 0.018513, 0.011108, 0.006665], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 1.595105, 'e_o_k': [0.345920, 0.207552, 0.124531, 0.074719, 0.044831], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 4.086998, 'e_o_k': [1.042601, 0.625561, 0.375337], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 10.112241, 'e_o_k': [2.579653, 1.547792, 0.928675], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 1.915959, 'e_o_k': [0.598737, 0.359242], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 1.005364, 'e_o_k': [0.314176, 0.188506], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 1.093498, 'e_o_k': [0.251263, 0.150758, 0.090455, 0.054273], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 21.458838, 'e_o_k': [5.474193, 3.284516, 1.970710], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
