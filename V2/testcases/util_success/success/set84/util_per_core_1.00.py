"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199992, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199992, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.614457, 'e_o_k': [0.049966, 0.039973, 0.031978, 0.025582, 0.020466, 0.016373], 'p_i': 10, 'u_i': 4.4319},
        {'id': 1, 'e_m': 6.393105, 'e_o_k': [0.570541, 0.456433, 0.365146, 0.292117, 0.233694], 'p_i': 20, 'u_i': 3.5005},
        {'id': 2, 'e_m': 3.706742, 'e_o_k': [0.376701, 0.301361, 0.241089, 0.192871], 'p_i': 40, 'u_i': 3.6064},
        {'id': 3, 'e_m': 33.192884, 'e_o_k': [2.962240, 2.369792, 1.895833, 1.516667, 1.213333], 'p_i': 80, 'u_i': 2.1318},
        {'id': 4, 'e_m': 13.502409, 'e_o_k': [1.097971, 0.878377, 0.702701, 0.562161, 0.449729, 0.359783], 'p_i': 40, 'u_i': 2.3435},
        {'id': 5, 'e_m': 0.192710, 'e_o_k': [0.017198, 0.013758, 0.011007, 0.008805, 0.007044], 'p_i': 10, 'u_i': 4.1320},
        {'id': 6, 'e_m': 30.548559, 'e_o_k': [5.091426, 4.073141], 'p_i': 80, 'u_i': 4.9104},
        {'id': 7, 'e_m': 3.726312, 'e_o_k': [0.621052, 0.496842], 'p_i': 10, 'u_i': 1.8351},
    ]
    B_BUDGET = 239.199992
    return processors, tasks, B_BUDGET
