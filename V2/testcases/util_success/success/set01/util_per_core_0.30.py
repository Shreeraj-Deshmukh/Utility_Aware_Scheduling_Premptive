"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760008, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760008, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.191731, 'e_o_k': [0.015591, 0.012473, 0.009978, 0.007983, 0.006386, 0.005109], 'p_i': 10, 'u_i': 4.5169},
        {'id': 1, 'e_m': 4.376202, 'e_o_k': [0.729367, 0.583494], 'p_i': 20, 'u_i': 3.9484},
        {'id': 2, 'e_m': 0.772522, 'e_o_k': [0.068942, 0.055154, 0.044123, 0.035299, 0.028239], 'p_i': 40, 'u_i': 3.8598},
        {'id': 3, 'e_m': 0.993778, 'e_o_k': [0.080811, 0.064649, 0.051719, 0.041375, 0.033100, 0.026480], 'p_i': 80, 'u_i': 3.9484},
        {'id': 4, 'e_m': 14.525907, 'e_o_k': [1.785972, 1.428778, 1.143022], 'p_i': 80, 'u_i': 4.6365},
        {'id': 5, 'e_m': 0.297439, 'e_o_k': [0.024187, 0.019349, 0.015480, 0.012384, 0.009907, 0.007926], 'p_i': 40, 'u_i': 4.7054},
        {'id': 6, 'e_m': 2.419746, 'e_o_k': [0.403291, 0.322633], 'p_i': 80, 'u_i': 3.2554},
        {'id': 7, 'e_m': 2.220497, 'e_o_k': [0.370083, 0.296066], 'p_i': 20, 'u_i': 3.5452},
    ]
    B_BUDGET = 71.760008
    return processors, tasks, B_BUDGET
