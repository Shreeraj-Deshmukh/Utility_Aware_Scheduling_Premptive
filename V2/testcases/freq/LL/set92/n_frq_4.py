"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 34, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "freq", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 34, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "freq", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.279536, 'e_o_k': [0.041578, 0.033262, 0.026610, 0.021288, 0.017030], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 0.807491, 'e_o_k': [0.109437, 0.087550, 0.070040, 0.056032, 0.044826, 0.035860], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 3.179023, 'e_o_k': [0.651439, 0.521151, 0.416921], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 7.775197, 'e_o_k': [1.316937, 1.053550, 0.842840, 0.674272], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.001832, 'e_o_k': [0.000509, 0.000407], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 1.937647, 'e_o_k': [0.397059, 0.317647, 0.254118], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 0.361320, 'e_o_k': [0.061199, 0.048959, 0.039167, 0.031334], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 3.778825, 'e_o_k': [0.640045, 0.512036, 0.409629, 0.327703], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET
