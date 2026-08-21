"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.237773, 'e_o_k': [0.184935, 0.147948], 'p_i': 10, 'u_i': 4.9795},
        {'id': 1, 'e_m': 2.303196, 'e_o_k': [1.791375, 1.433100], 'p_i': 20, 'u_i': 4.9448},
        {'id': 2, 'e_m': 7.567437, 'e_o_k': [5.885785, 4.708628], 'p_i': 40, 'u_i': 4.4554},
        {'id': 3, 'e_m': 20.093036, 'e_o_k': [15.627917, 12.502334], 'p_i': 80, 'u_i': 2.2591},
        {'id': 4, 'e_m': 0.219572, 'e_o_k': [0.170778, 0.136622], 'p_i': 10, 'u_i': 2.7803},
        {'id': 5, 'e_m': 9.972517, 'e_o_k': [7.756402, 6.205122], 'p_i': 80, 'u_i': 1.7696},
        {'id': 6, 'e_m': 3.107005, 'e_o_k': [2.416559, 1.933247], 'p_i': 80, 'u_i': 4.8086},
        {'id': 7, 'e_m': 0.705255, 'e_o_k': [0.548532, 0.438826], 'p_i': 20, 'u_i': 1.4894},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET
