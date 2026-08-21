"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 27, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "freq", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 27, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "freq", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.201488, 'e_o_k': [0.029969, 0.023975, 0.019180, 0.015344, 0.012275], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 1.441830, 'e_o_k': [0.195408, 0.156326, 0.125061, 0.100049, 0.080039, 0.064031], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 8.661890, 'e_o_k': [2.406081, 1.924865], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 8.902172, 'e_o_k': [2.472826, 1.978261], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 5.993625, 'e_o_k': [1.664896, 1.331917], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 4.342413, 'e_o_k': [0.588518, 0.470814, 0.376651, 0.301321, 0.241057, 0.192845], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 1.301354, 'e_o_k': [0.361487, 0.289190], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 3.654332, 'e_o_k': [0.748838, 0.599071, 0.479257], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
