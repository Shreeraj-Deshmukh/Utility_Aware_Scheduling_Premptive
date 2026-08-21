"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 49.679997, "H": 80, "J": 23, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.7, "seed": 1086, "set": 86, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}
"""

_SPEC = '{"B": 49.679997, "H": 80, "J": 23, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.7, "seed": 1086, "set": 86, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.050222, 'e_o_k': [0.010291, 0.008233, 0.006586], 'p_i': 10, 'u_i': 2.4144},
        {'id': 1, 'e_m': 0.206926, 'e_o_k': [0.057479, 0.045983], 'p_i': 20, 'u_i': 2.6559},
        {'id': 2, 'e_m': 1.190379, 'e_o_k': [0.177055, 0.141644, 0.113315, 0.090652, 0.072522], 'p_i': 40, 'u_i': 2.8681},
        {'id': 3, 'e_m': 6.971948, 'e_o_k': [1.936652, 1.549322], 'p_i': 80, 'u_i': 1.8896},
        {'id': 4, 'e_m': 0.550862, 'e_o_k': [0.081935, 0.065548, 0.052438, 0.041950, 0.033560], 'p_i': 20, 'u_i': 1.6645},
        {'id': 5, 'e_m': 0.291867, 'e_o_k': [0.043412, 0.034730, 0.027784, 0.022227, 0.017782], 'p_i': 40, 'u_i': 1.3774},
        {'id': 6, 'e_m': 1.611679, 'e_o_k': [0.447689, 0.358151], 'p_i': 80, 'u_i': 1.9412},
        {'id': 7, 'e_m': 17.018957, 'e_o_k': [4.727488, 3.781990], 'p_i': 80, 'u_i': 2.2237},
    ]
    B_BUDGET = 49.679997
    return processors, tasks, B_BUDGET
