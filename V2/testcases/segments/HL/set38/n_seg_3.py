"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400015, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400015, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.141191, 'e_o_k': [0.438769, 0.351015, 0.280812], 'p_i': 10, 'u_i': 2.6411},
        {'id': 1, 'e_m': 2.391844, 'e_o_k': [0.490132, 0.392106, 0.313684], 'p_i': 20, 'u_i': 4.9928},
        {'id': 2, 'e_m': 6.358508, 'e_o_k': [1.302973, 1.042378, 0.833903], 'p_i': 40, 'u_i': 3.9733},
        {'id': 3, 'e_m': 4.020499, 'e_o_k': [0.823873, 0.659098, 0.527279], 'p_i': 80, 'u_i': 1.2745},
        {'id': 4, 'e_m': 0.589014, 'e_o_k': [0.120700, 0.096560, 0.077248], 'p_i': 10, 'u_i': 1.8926},
        {'id': 5, 'e_m': 2.500170, 'e_o_k': [0.512330, 0.409864, 0.327891], 'p_i': 40, 'u_i': 4.4301},
        {'id': 6, 'e_m': 4.620754, 'e_o_k': [0.946876, 0.757501, 0.606000], 'p_i': 40, 'u_i': 2.8023},
        {'id': 7, 'e_m': 0.201453, 'e_o_k': [0.041281, 0.033025, 0.026420], 'p_i': 10, 'u_i': 1.0101},
    ]
    B_BUDGET = 110.400015
    return processors, tasks, B_BUDGET
