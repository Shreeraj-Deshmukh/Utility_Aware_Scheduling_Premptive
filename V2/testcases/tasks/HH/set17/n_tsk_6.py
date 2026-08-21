"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639986, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639986, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.088441, 'e_o_k': [0.846565, 0.677252], 'p_i': 10, 'u_i': 3.6581},
        {'id': 1, 'e_m': 1.482591, 'e_o_k': [0.617452, 0.493962, 0.395169, 0.316136, 0.252908], 'p_i': 20, 'u_i': 4.4037},
        {'id': 2, 'e_m': 10.472843, 'e_o_k': [3.974212, 3.179370, 2.543496, 2.034796, 1.627837, 1.302270], 'p_i': 40, 'u_i': 3.5196},
        {'id': 3, 'e_m': 19.699905, 'e_o_k': [7.475677, 5.980542, 4.784434, 3.827547, 3.062037, 2.449630], 'p_i': 80, 'u_i': 2.9192},
        {'id': 4, 'e_m': 2.996690, 'e_o_k': [1.421195, 1.136956, 0.909565, 0.727652], 'p_i': 40, 'u_i': 2.0454},
        {'id': 5, 'e_m': 1.361566, 'e_o_k': [0.516684, 0.413347, 0.330678, 0.264542, 0.211634, 0.169307], 'p_i': 40, 'u_i': 2.8602},
    ]
    B_BUDGET = 176.639986
    return processors, tasks, B_BUDGET
