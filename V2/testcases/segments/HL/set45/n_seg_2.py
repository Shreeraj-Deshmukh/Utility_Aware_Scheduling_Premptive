"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.095169, 'e_o_k': [0.026436, 0.021149], 'p_i': 10, 'u_i': 1.5331},
        {'id': 1, 'e_m': 0.997826, 'e_o_k': [0.277174, 0.221739], 'p_i': 20, 'u_i': 4.3760},
        {'id': 2, 'e_m': 0.022485, 'e_o_k': [0.006246, 0.004997], 'p_i': 40, 'u_i': 3.1042},
        {'id': 3, 'e_m': 2.231053, 'e_o_k': [0.619737, 0.495789], 'p_i': 80, 'u_i': 3.0115},
        {'id': 4, 'e_m': 6.335688, 'e_o_k': [1.759913, 1.407931], 'p_i': 80, 'u_i': 1.0080},
        {'id': 5, 'e_m': 9.200112, 'e_o_k': [2.555587, 2.044469], 'p_i': 80, 'u_i': 3.4234},
        {'id': 6, 'e_m': 6.435349, 'e_o_k': [1.787597, 1.430077], 'p_i': 80, 'u_i': 1.9989},
        {'id': 7, 'e_m': 4.375021, 'e_o_k': [1.215284, 0.972227], 'p_i': 10, 'u_i': 4.9421},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
