"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.219440, 'e_o_k': [0.156743, 0.094046, 0.056427], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 1.145357, 'e_o_k': [0.672790, 0.403674, 0.242204, 0.145323, 0.087194, 0.052316], 'p_i': 20, 'u_i': 2.8306},
        {'id': 2, 'e_m': 11.261726, 'e_o_k': [8.044090, 4.826454, 2.895872], 'p_i': 40, 'u_i': 2.9234},
        {'id': 3, 'e_m': 7.430483, 'e_o_k': [5.307488, 3.184493, 1.910696], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 2.663123, 'e_o_k': [1.902230, 1.141338, 0.684803], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 3.271381, 'e_o_k': [2.862458, 1.717475], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.028377, 'e_o_k': [0.016669, 0.010001, 0.006001, 0.003600, 0.002160, 0.001296], 'p_i': 40, 'u_i': 4.5772},
        {'id': 7, 'e_m': 1.307139, 'e_o_k': [0.793717, 0.476230, 0.285738, 0.171443, 0.102866], 'p_i': 10, 'u_i': 4.4816},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
