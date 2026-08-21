"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319992, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319992, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.153313, 'e_o_k': [0.098639, 0.059183, 0.035510, 0.021306], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.148369, 'e_o_k': [0.087153, 0.052292, 0.031375, 0.018825, 0.011295, 0.006777], 'p_i': 20, 'u_i': 2.3478},
        {'id': 2, 'e_m': 2.270223, 'e_o_k': [1.621588, 0.972953, 0.583772], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 7.275677, 'e_o_k': [4.417916, 2.650750, 1.590450, 0.954270, 0.572562], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 2.680502, 'e_o_k': [2.345439, 1.407263], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 1.468106, 'e_o_k': [0.862374, 0.517424, 0.310455, 0.186273, 0.111764, 0.067058], 'p_i': 40, 'u_i': 2.1935},
        {'id': 6, 'e_m': 0.569881, 'e_o_k': [0.407058, 0.244235, 0.146541], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.303269, 'e_o_k': [0.265360, 0.159216], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 88.319992
    return processors, tasks, B_BUDGET
