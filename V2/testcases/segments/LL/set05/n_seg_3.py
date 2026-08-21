"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.394847, 'e_o_k': [0.080911, 0.064729, 0.051783], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.122647, 'e_o_k': [0.025133, 0.020106, 0.016085], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 1.655397, 'e_o_k': [0.339221, 0.271377, 0.217101], 'p_i': 40, 'u_i': 2.1879},
        {'id': 3, 'e_m': 0.814260, 'e_o_k': [0.166856, 0.133485, 0.106788], 'p_i': 80, 'u_i': 2.3607},
        {'id': 4, 'e_m': 1.025576, 'e_o_k': [0.210159, 0.168127, 0.134502], 'p_i': 20, 'u_i': 2.0600},
        {'id': 5, 'e_m': 0.055175, 'e_o_k': [0.011306, 0.009045, 0.007236], 'p_i': 80, 'u_i': 2.1803},
        {'id': 6, 'e_m': 1.611854, 'e_o_k': [0.330298, 0.264238, 0.211391], 'p_i': 10, 'u_i': 4.5157},
        {'id': 7, 'e_m': 3.586638, 'e_o_k': [0.734967, 0.587973, 0.470379], 'p_i': 40, 'u_i': 4.4957},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
