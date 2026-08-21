"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280002, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280002, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.833026, 'e_o_k': [0.084657, 0.067726, 0.054181, 0.043344], 'p_i': 10, 'u_i': 3.8210},
        {'id': 1, 'e_m': 5.063402, 'e_o_k': [0.514573, 0.411659, 0.329327, 0.263462], 'p_i': 20, 'u_i': 3.6417},
        {'id': 2, 'e_m': 10.109600, 'e_o_k': [0.902213, 0.721771, 0.577416, 0.461933, 0.369547], 'p_i': 40, 'u_i': 4.9240},
        {'id': 3, 'e_m': 3.058182, 'e_o_k': [0.376006, 0.300805, 0.240644], 'p_i': 80, 'u_i': 4.7730},
        {'id': 4, 'e_m': 10.372056, 'e_o_k': [1.054071, 0.843257, 0.674605, 0.539684], 'p_i': 80, 'u_i': 2.1774},
        {'id': 5, 'e_m': 4.361031, 'e_o_k': [0.443194, 0.354555, 0.283644, 0.226915], 'p_i': 10, 'u_i': 1.8820},
        {'id': 6, 'e_m': 1.104352, 'e_o_k': [0.184059, 0.147247], 'p_i': 10, 'u_i': 3.8453},
        {'id': 7, 'e_m': 4.963711, 'e_o_k': [0.504442, 0.403554, 0.322843, 0.258274], 'p_i': 10, 'u_i': 2.4470},
    ]
    B_BUDGET = 215.280002
    return processors, tasks, B_BUDGET
