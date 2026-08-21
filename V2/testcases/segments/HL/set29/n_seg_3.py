"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.555176, 'e_o_k': [0.113766, 0.091012, 0.072810], 'p_i': 10, 'u_i': 2.4751},
        {'id': 1, 'e_m': 0.851460, 'e_o_k': [0.174480, 0.139584, 0.111667], 'p_i': 20, 'u_i': 3.6644},
        {'id': 2, 'e_m': 3.395703, 'e_o_k': [0.695841, 0.556673, 0.445338], 'p_i': 40, 'u_i': 2.2976},
        {'id': 3, 'e_m': 3.482314, 'e_o_k': [0.713589, 0.570871, 0.456697], 'p_i': 80, 'u_i': 4.8639},
        {'id': 4, 'e_m': 4.033383, 'e_o_k': [0.826513, 0.661210, 0.528968], 'p_i': 40, 'u_i': 4.5045},
        {'id': 5, 'e_m': 2.789347, 'e_o_k': [0.571587, 0.457270, 0.365816], 'p_i': 80, 'u_i': 1.0020},
        {'id': 6, 'e_m': 3.567276, 'e_o_k': [0.730999, 0.584799, 0.467840], 'p_i': 40, 'u_i': 4.9529},
        {'id': 7, 'e_m': 3.486046, 'e_o_k': [0.714354, 0.571483, 0.457186], 'p_i': 10, 'u_i': 2.3587},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
