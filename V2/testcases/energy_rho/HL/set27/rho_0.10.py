"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 77.28, "H": 80, "J": 34, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.1, "seed": 1027, "set": 27, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.10"}
"""

_SPEC = '{"B": 77.28, "H": 80, "J": 34, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.1, "seed": 1027, "set": 27, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.415674, 'e_o_k': [0.578536, 0.462828, 0.370263, 0.296210], 'p_i': 10, 'u_i': 3.9517},
        {'id': 1, 'e_m': 0.148832, 'e_o_k': [0.022137, 0.017710, 0.014168, 0.011334, 0.009067], 'p_i': 20, 'u_i': 3.7467},
        {'id': 2, 'e_m': 2.086145, 'e_o_k': [0.310291, 0.248232, 0.198586, 0.158869, 0.127095], 'p_i': 40, 'u_i': 4.6120},
        {'id': 3, 'e_m': 0.844474, 'e_o_k': [0.234576, 0.187661], 'p_i': 80, 'u_i': 4.9202},
        {'id': 4, 'e_m': 1.893474, 'e_o_k': [0.525965, 0.420772], 'p_i': 80, 'u_i': 4.2451},
        {'id': 5, 'e_m': 1.089996, 'e_o_k': [0.302777, 0.242221], 'p_i': 10, 'u_i': 4.7909},
        {'id': 6, 'e_m': 2.548948, 'e_o_k': [0.431732, 0.345386, 0.276309, 0.221047], 'p_i': 10, 'u_i': 3.3523},
        {'id': 7, 'e_m': 0.028745, 'e_o_k': [0.004869, 0.003895, 0.003116, 0.002493], 'p_i': 40, 'u_i': 1.0347},
    ]
    B_BUDGET = 77.280000
    return processors, tasks, B_BUDGET
