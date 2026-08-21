"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200002, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200002, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.266601, 'e_o_k': [0.155730, 0.124584, 0.099667], 'p_i': 10, 'u_i': 2.2059},
        {'id': 1, 'e_m': 4.048688, 'e_o_k': [0.411452, 0.329162, 0.263329, 0.210663], 'p_i': 20, 'u_i': 4.0638},
        {'id': 2, 'e_m': 13.264398, 'e_o_k': [1.183758, 0.947006, 0.757605, 0.606084, 0.484867], 'p_i': 40, 'u_i': 4.2047},
        {'id': 3, 'e_m': 24.886444, 'e_o_k': [4.147741, 3.318193], 'p_i': 80, 'u_i': 3.2452},
        {'id': 4, 'e_m': 6.914945, 'e_o_k': [0.562300, 0.449840, 0.359872, 0.287898, 0.230318, 0.184255], 'p_i': 20, 'u_i': 3.8255},
        {'id': 5, 'e_m': 6.831778, 'e_o_k': [1.138630, 0.910904], 'p_i': 80, 'u_i': 2.9448},
        {'id': 6, 'e_m': 3.114061, 'e_o_k': [0.253225, 0.202580, 0.162064, 0.129651, 0.103721, 0.082977], 'p_i': 10, 'u_i': 2.8728},
        {'id': 7, 'e_m': 5.713288, 'e_o_k': [0.509872, 0.407898, 0.326318, 0.261055, 0.208844], 'p_i': 20, 'u_i': 3.0771},
    ]
    B_BUDGET = 239.200002
    return processors, tasks, B_BUDGET
