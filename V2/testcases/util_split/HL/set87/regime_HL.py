"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 33, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_split", "util_per_core": 0.4, "value": "HL"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 33, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_split", "util_per_core": 0.4, "value": "HL"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.644057, 'e_o_k': [0.244535, 0.195628, 0.156502, 0.125202, 0.100162], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.317213, 'e_o_k': [0.065003, 0.052002, 0.041602], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 1.169415, 'e_o_k': [0.173937, 0.139150, 0.111320, 0.089056, 0.071245], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 12.303905, 'e_o_k': [2.521292, 2.017034, 1.613627], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 2.417694, 'e_o_k': [0.409501, 0.327601, 0.262081, 0.209665], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 1.761783, 'e_o_k': [0.489384, 0.391507], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 1.036762, 'e_o_k': [0.154207, 0.123365, 0.098692, 0.078954, 0.063163], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 2.274347, 'e_o_k': [0.338283, 0.270627, 0.216501, 0.173201, 0.138561], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
