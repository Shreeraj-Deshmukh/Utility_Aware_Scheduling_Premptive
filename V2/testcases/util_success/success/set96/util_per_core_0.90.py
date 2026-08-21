"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280002, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280002, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.029438, 'e_o_k': [0.327660, 0.262128, 0.209703, 0.167762, 0.134210, 0.107368], 'p_i': 10, 'u_i': 2.0949},
        {'id': 1, 'e_m': 4.287133, 'e_o_k': [0.714522, 0.571618], 'p_i': 20, 'u_i': 3.1382},
        {'id': 2, 'e_m': 3.573651, 'e_o_k': [0.363176, 0.290541, 0.232433, 0.185946], 'p_i': 40, 'u_i': 1.0740},
        {'id': 3, 'e_m': 5.978451, 'e_o_k': [0.735055, 0.588044, 0.470435], 'p_i': 80, 'u_i': 1.9073},
        {'id': 4, 'e_m': 1.371901, 'e_o_k': [0.139421, 0.111537, 0.089229, 0.071383], 'p_i': 80, 'u_i': 4.7552},
        {'id': 5, 'e_m': 2.567211, 'e_o_k': [0.208757, 0.167006, 0.133605, 0.106884, 0.085507, 0.068406], 'p_i': 80, 'u_i': 2.5856},
        {'id': 6, 'e_m': 4.962901, 'e_o_k': [0.610193, 0.488154, 0.390523], 'p_i': 10, 'u_i': 4.0663},
        {'id': 7, 'e_m': 4.730987, 'e_o_k': [0.581679, 0.465343, 0.372274], 'p_i': 10, 'u_i': 2.6136},
    ]
    B_BUDGET = 215.280002
    return processors, tasks, B_BUDGET
