"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280011, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280011, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.090991, 'e_o_k': [0.502991, 0.402393, 0.321914], 'p_i': 10, 'u_i': 2.4225},
        {'id': 1, 'e_m': 0.342742, 'e_o_k': [0.027871, 0.022297, 0.017837, 0.014270, 0.011416, 0.009133], 'p_i': 20, 'u_i': 3.0832},
        {'id': 2, 'e_m': 2.433405, 'e_o_k': [0.217165, 0.173732, 0.138986, 0.111188, 0.088951], 'p_i': 40, 'u_i': 3.4868},
        {'id': 3, 'e_m': 9.562386, 'e_o_k': [1.593731, 1.274985], 'p_i': 80, 'u_i': 3.8765},
        {'id': 4, 'e_m': 17.815684, 'e_o_k': [1.589929, 1.271943, 1.017555, 0.814044, 0.651235], 'p_i': 40, 'u_i': 3.4288},
        {'id': 5, 'e_m': 7.413069, 'e_o_k': [0.911443, 0.729154, 0.583323], 'p_i': 20, 'u_i': 3.2994},
        {'id': 6, 'e_m': 2.742010, 'e_o_k': [0.278660, 0.222928, 0.178342, 0.142674], 'p_i': 20, 'u_i': 1.7707},
        {'id': 7, 'e_m': 9.610110, 'e_o_k': [0.976637, 0.781310, 0.625048, 0.500038], 'p_i': 40, 'u_i': 4.2984},
    ]
    B_BUDGET = 215.280011
    return processors, tasks, B_BUDGET
