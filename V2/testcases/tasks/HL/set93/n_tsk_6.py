"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400013, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400013, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.555997, 'e_o_k': [0.210881, 0.168705, 0.134964, 0.107971, 0.086377, 0.069101], 'p_i': 10, 'u_i': 3.2097},
        {'id': 1, 'e_m': 1.561617, 'e_o_k': [0.320003, 0.256003, 0.204802], 'p_i': 20, 'u_i': 3.3970},
        {'id': 2, 'e_m': 2.401288, 'e_o_k': [0.325441, 0.260353, 0.208282, 0.166626, 0.133301, 0.106641], 'p_i': 40, 'u_i': 4.0644},
        {'id': 3, 'e_m': 15.726898, 'e_o_k': [2.339198, 1.871359, 1.497087, 1.197669, 0.958136], 'p_i': 80, 'u_i': 4.4775},
        {'id': 4, 'e_m': 2.610152, 'e_o_k': [0.442099, 0.353679, 0.282943, 0.226355], 'p_i': 10, 'u_i': 1.6225},
        {'id': 5, 'e_m': 3.894872, 'e_o_k': [0.527863, 0.422291, 0.337833, 0.270266, 0.216213, 0.172970], 'p_i': 80, 'u_i': 1.5082},
    ]
    B_BUDGET = 110.400013
    return processors, tasks, B_BUDGET
