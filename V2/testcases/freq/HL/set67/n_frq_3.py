"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 24, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "freq", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 24, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "freq", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.622255, 'e_o_k': [0.538769, 0.431016, 0.344812, 0.275850, 0.220680], 'p_i': 10, 'u_i': 3.4311},
        {'id': 1, 'e_m': 0.101434, 'e_o_k': [0.017180, 0.013744, 0.010996, 0.008796], 'p_i': 20, 'u_i': 3.8774},
        {'id': 2, 'e_m': 5.088426, 'e_o_k': [1.413452, 1.130761], 'p_i': 40, 'u_i': 3.3220},
        {'id': 3, 'e_m': 2.359092, 'e_o_k': [0.655303, 0.524243], 'p_i': 80, 'u_i': 2.5309},
        {'id': 4, 'e_m': 3.488235, 'e_o_k': [0.714802, 0.571842, 0.457473], 'p_i': 40, 'u_i': 3.7128},
        {'id': 5, 'e_m': 1.158934, 'e_o_k': [0.321926, 0.257541], 'p_i': 20, 'u_i': 4.9574},
        {'id': 6, 'e_m': 9.098933, 'e_o_k': [1.864535, 1.491628, 1.193303], 'p_i': 80, 'u_i': 3.9330},
        {'id': 7, 'e_m': 0.684572, 'e_o_k': [0.140281, 0.112225, 0.089780], 'p_i': 40, 'u_i': 3.5882},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
