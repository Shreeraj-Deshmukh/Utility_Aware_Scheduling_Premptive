"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 52.256, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.3, "seed": 1090, "set": 90, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.30"}
"""

_SPEC = '{"B": 52.256, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.3, "seed": 1090, "set": 90, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.427962, 'e_o_k': [0.178233, 0.142586, 0.114069, 0.091255, 0.073004], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 1.031123, 'e_o_k': [0.391288, 0.313031, 0.250424, 0.200340, 0.160272, 0.128217], 'p_i': 20, 'u_i': 3.3367},
        {'id': 2, 'e_m': 0.898123, 'e_o_k': [0.515316, 0.412253, 0.329803], 'p_i': 40, 'u_i': 4.5472},
        {'id': 3, 'e_m': 0.364547, 'e_o_k': [0.172888, 0.138311, 0.110648, 0.088519], 'p_i': 80, 'u_i': 1.6834},
        {'id': 4, 'e_m': 1.110849, 'e_o_k': [0.863994, 0.691195], 'p_i': 40, 'u_i': 3.8684},
        {'id': 5, 'e_m': 6.962867, 'e_o_k': [5.415563, 4.332450], 'p_i': 40, 'u_i': 4.7513},
        {'id': 6, 'e_m': 2.975430, 'e_o_k': [1.129110, 0.903288, 0.722630, 0.578104, 0.462483, 0.369987], 'p_i': 40, 'u_i': 2.4512},
        {'id': 7, 'e_m': 0.024091, 'e_o_k': [0.018737, 0.014990], 'p_i': 10, 'u_i': 1.4858},
    ]
    B_BUDGET = 52.256000
    return processors, tasks, B_BUDGET
