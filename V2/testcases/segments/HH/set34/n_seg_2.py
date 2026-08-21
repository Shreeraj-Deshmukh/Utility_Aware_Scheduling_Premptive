"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.219440, 'e_o_k': [0.170675, 0.136540], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 1.145357, 'e_o_k': [0.890833, 0.712667], 'p_i': 20, 'u_i': 3.8785},
        {'id': 2, 'e_m': 11.261726, 'e_o_k': [8.759120, 7.007296], 'p_i': 40, 'u_i': 2.8542},
        {'id': 3, 'e_m': 7.430483, 'e_o_k': [5.779264, 4.623412], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 2.663123, 'e_o_k': [2.071318, 1.657054], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 3.271381, 'e_o_k': [2.544407, 2.035526], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.028377, 'e_o_k': [0.022071, 0.017657], 'p_i': 40, 'u_i': 2.8369},
        {'id': 7, 'e_m': 1.307139, 'e_o_k': [1.016664, 0.813331], 'p_i': 10, 'u_i': 1.1432},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
