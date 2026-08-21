"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280002, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280002, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.395512, 'e_o_k': [0.565919, 0.452735], 'p_i': 10, 'u_i': 4.8512},
        {'id': 1, 'e_m': 1.350580, 'e_o_k': [0.225097, 0.180077], 'p_i': 20, 'u_i': 2.1049},
        {'id': 2, 'e_m': 11.772087, 'e_o_k': [1.196350, 0.957080, 0.765664, 0.612531], 'p_i': 40, 'u_i': 2.1681},
        {'id': 3, 'e_m': 18.981668, 'e_o_k': [1.929031, 1.543225, 1.234580, 0.987664], 'p_i': 80, 'u_i': 3.4225},
        {'id': 4, 'e_m': 0.716397, 'e_o_k': [0.058255, 0.046604, 0.037283, 0.029827, 0.023861, 0.019089], 'p_i': 40, 'u_i': 4.5153},
        {'id': 5, 'e_m': 4.316905, 'e_o_k': [0.530767, 0.424614, 0.339691], 'p_i': 10, 'u_i': 3.2535},
        {'id': 6, 'e_m': 7.075555, 'e_o_k': [0.719060, 0.575248, 0.460199, 0.368159], 'p_i': 40, 'u_i': 2.8656},
        {'id': 7, 'e_m': 2.348575, 'e_o_k': [0.238676, 0.190941, 0.152753, 0.122202], 'p_i': 10, 'u_i': 3.1003},
    ]
    B_BUDGET = 215.280002
    return processors, tasks, B_BUDGET
