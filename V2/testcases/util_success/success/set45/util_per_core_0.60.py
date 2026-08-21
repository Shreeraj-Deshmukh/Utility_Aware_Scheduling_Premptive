"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520017, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520017, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.364357, 'e_o_k': [0.227393, 0.181914], 'p_i': 10, 'u_i': 3.2915},
        {'id': 1, 'e_m': 2.474424, 'e_o_k': [0.251466, 0.201173, 0.160938, 0.128750], 'p_i': 20, 'u_i': 3.4234},
        {'id': 2, 'e_m': 2.038058, 'e_o_k': [0.207120, 0.165696, 0.132557, 0.106045], 'p_i': 40, 'u_i': 1.9989},
        {'id': 3, 'e_m': 12.388500, 'e_o_k': [1.007392, 0.805913, 0.644731, 0.515785, 0.412628, 0.330102], 'p_i': 80, 'u_i': 4.1665},
        {'id': 4, 'e_m': 4.577802, 'e_o_k': [0.762967, 0.610374], 'p_i': 20, 'u_i': 2.8771},
        {'id': 5, 'e_m': 1.545201, 'e_o_k': [0.157033, 0.125626, 0.100501, 0.080401], 'p_i': 20, 'u_i': 3.3920},
        {'id': 6, 'e_m': 0.667482, 'e_o_k': [0.111247, 0.088998], 'p_i': 10, 'u_i': 1.7352},
        {'id': 7, 'e_m': 7.222742, 'e_o_k': [0.644581, 0.515665, 0.412532, 0.330025, 0.264020], 'p_i': 20, 'u_i': 3.3959},
    ]
    B_BUDGET = 143.520017
    return processors, tasks, B_BUDGET
