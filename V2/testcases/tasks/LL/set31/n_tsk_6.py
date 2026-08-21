"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.274433, 'e_o_k': [0.046483, 0.037186, 0.029749, 0.023799], 'p_i': 10, 'u_i': 2.8575},
        {'id': 1, 'e_m': 1.031563, 'e_o_k': [0.153433, 0.122747, 0.098197, 0.078558, 0.062846], 'p_i': 20, 'u_i': 2.8209},
        {'id': 2, 'e_m': 0.135038, 'e_o_k': [0.037510, 0.030008], 'p_i': 40, 'u_i': 2.9332},
        {'id': 3, 'e_m': 2.013335, 'e_o_k': [0.412569, 0.330055, 0.264044], 'p_i': 80, 'u_i': 1.0372},
        {'id': 4, 'e_m': 2.006057, 'e_o_k': [0.411077, 0.328862, 0.263089], 'p_i': 10, 'u_i': 1.7921},
        {'id': 5, 'e_m': 3.673209, 'e_o_k': [0.497822, 0.398257, 0.318606, 0.254885, 0.203908, 0.163126], 'p_i': 40, 'u_i': 1.1296},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
