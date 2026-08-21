"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200008, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200008, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.479783, 'e_o_k': [0.364281, 0.291425, 0.233140, 0.186512, 0.149210, 0.119368], 'p_i': 10, 'u_i': 2.8037},
        {'id': 1, 'e_m': 0.984169, 'e_o_k': [0.100017, 0.080014, 0.064011, 0.051209], 'p_i': 20, 'u_i': 4.7578},
        {'id': 2, 'e_m': 5.765967, 'e_o_k': [0.960995, 0.768796], 'p_i': 40, 'u_i': 1.7165},
        {'id': 3, 'e_m': 36.705968, 'e_o_k': [2.984807, 2.387846, 1.910277, 1.528221, 1.222577, 0.978062], 'p_i': 80, 'u_i': 2.0036},
        {'id': 4, 'e_m': 5.616630, 'e_o_k': [0.690569, 0.552455, 0.441964], 'p_i': 20, 'u_i': 1.4212},
        {'id': 5, 'e_m': 1.973675, 'e_o_k': [0.242665, 0.194132, 0.155306], 'p_i': 10, 'u_i': 3.1256},
        {'id': 6, 'e_m': 5.771112, 'e_o_k': [0.586495, 0.469196, 0.375357, 0.300285], 'p_i': 80, 'u_i': 1.0663},
        {'id': 7, 'e_m': 6.990031, 'e_o_k': [0.623813, 0.499050, 0.399240, 0.319392, 0.255514], 'p_i': 20, 'u_i': 3.8936},
    ]
    B_BUDGET = 239.200008
    return processors, tasks, B_BUDGET
