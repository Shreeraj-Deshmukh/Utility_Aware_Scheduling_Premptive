"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440013, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440013, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.591750, 'e_o_k': [0.265292, 0.212233], 'p_i': 10, 'u_i': 3.2915},
        {'id': 1, 'e_m': 2.886828, 'e_o_k': [0.293377, 0.234701, 0.187761, 0.150209], 'p_i': 20, 'u_i': 3.4234},
        {'id': 2, 'e_m': 2.377734, 'e_o_k': [0.241640, 0.193312, 0.154649, 0.123720], 'p_i': 40, 'u_i': 1.9989},
        {'id': 3, 'e_m': 14.453250, 'e_o_k': [1.175290, 0.940232, 0.752186, 0.601749, 0.481399, 0.385119], 'p_i': 80, 'u_i': 4.1665},
        {'id': 4, 'e_m': 5.340769, 'e_o_k': [0.890128, 0.712102], 'p_i': 20, 'u_i': 2.8771},
        {'id': 5, 'e_m': 1.802735, 'e_o_k': [0.183205, 0.146564, 0.117251, 0.093801], 'p_i': 20, 'u_i': 3.3920},
        {'id': 6, 'e_m': 0.778729, 'e_o_k': [0.129788, 0.103830], 'p_i': 10, 'u_i': 1.7352},
        {'id': 7, 'e_m': 8.426533, 'e_o_k': [0.752011, 0.601609, 0.481287, 0.385030, 0.308024], 'p_i': 20, 'u_i': 3.3959},
    ]
    B_BUDGET = 167.440013
    return processors, tasks, B_BUDGET
