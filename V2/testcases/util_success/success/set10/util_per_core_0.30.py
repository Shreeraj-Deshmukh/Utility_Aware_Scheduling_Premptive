"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760016, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760016, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.332418, 'e_o_k': [0.027031, 0.021625, 0.017300, 0.013840, 0.011072, 0.008858], 'p_i': 10, 'u_i': 3.7777},
        {'id': 1, 'e_m': 0.288778, 'e_o_k': [0.025771, 0.020617, 0.016494, 0.013195, 0.010556], 'p_i': 20, 'u_i': 2.9102},
        {'id': 2, 'e_m': 5.390214, 'e_o_k': [0.547786, 0.438229, 0.350583, 0.280466], 'p_i': 40, 'u_i': 3.0744},
        {'id': 3, 'e_m': 15.465534, 'e_o_k': [2.577589, 2.062071], 'p_i': 80, 'u_i': 3.1102},
        {'id': 4, 'e_m': 1.088655, 'e_o_k': [0.088526, 0.070821, 0.056657, 0.045325, 0.036260, 0.029008], 'p_i': 20, 'u_i': 3.9746},
        {'id': 5, 'e_m': 1.009725, 'e_o_k': [0.124147, 0.099317, 0.079454], 'p_i': 10, 'u_i': 1.5757},
        {'id': 6, 'e_m': 1.550953, 'e_o_k': [0.190691, 0.152553, 0.122042], 'p_i': 40, 'u_i': 4.9941},
        {'id': 7, 'e_m': 1.202630, 'e_o_k': [0.200438, 0.160351], 'p_i': 40, 'u_i': 1.7632},
    ]
    B_BUDGET = 71.760016
    return processors, tasks, B_BUDGET
