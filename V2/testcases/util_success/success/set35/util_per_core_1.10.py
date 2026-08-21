"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.167511, 'e_o_k': [0.338888, 0.271111, 0.216888, 0.173511, 0.138809, 0.111047], 'p_i': 10, 'u_i': 3.9981},
        {'id': 1, 'e_m': 7.582600, 'e_o_k': [0.770589, 0.616472, 0.493177, 0.394542], 'p_i': 20, 'u_i': 1.1221},
        {'id': 2, 'e_m': 10.908520, 'e_o_k': [1.341212, 1.072969, 0.858375], 'p_i': 40, 'u_i': 1.0173},
        {'id': 3, 'e_m': 23.338391, 'e_o_k': [3.889732, 3.111785], 'p_i': 80, 'u_i': 4.7591},
        {'id': 4, 'e_m': 10.868318, 'e_o_k': [1.104504, 0.883603, 0.706882, 0.565506], 'p_i': 80, 'u_i': 4.6573},
        {'id': 5, 'e_m': 28.818182, 'e_o_k': [3.543219, 2.834575, 2.267660], 'p_i': 80, 'u_i': 3.1574},
        {'id': 6, 'e_m': 2.890354, 'e_o_k': [0.235034, 0.188027, 0.150422, 0.120337, 0.096270, 0.077016], 'p_i': 10, 'u_i': 2.6010},
        {'id': 7, 'e_m': 1.091187, 'e_o_k': [0.134162, 0.107330, 0.085864], 'p_i': 20, 'u_i': 2.4102},
    ]
    B_BUDGET = 263.120001
    return processors, tasks, B_BUDGET
