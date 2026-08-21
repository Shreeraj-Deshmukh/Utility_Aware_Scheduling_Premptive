"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320015, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320015, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.427962, 'e_o_k': [0.259866, 0.155920, 0.093552, 0.056131, 0.033679], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 1.031123, 'e_o_k': [0.605688, 0.363413, 0.218048, 0.130829, 0.078497, 0.047098], 'p_i': 20, 'u_i': 3.3367},
        {'id': 2, 'e_m': 0.898123, 'e_o_k': [0.641516, 0.384910, 0.230946], 'p_i': 40, 'u_i': 4.5472},
        {'id': 3, 'e_m': 0.364547, 'e_o_k': [0.234543, 0.140726, 0.084436, 0.050661], 'p_i': 80, 'u_i': 1.6834},
        {'id': 4, 'e_m': 1.110849, 'e_o_k': [0.971993, 0.583196], 'p_i': 40, 'u_i': 3.8684},
        {'id': 5, 'e_m': 6.962867, 'e_o_k': [6.092508, 3.655505], 'p_i': 40, 'u_i': 4.7513},
        {'id': 6, 'e_m': 2.975430, 'e_o_k': [1.747786, 1.048671, 0.629203, 0.377522, 0.226513, 0.135908], 'p_i': 40, 'u_i': 2.4512},
        {'id': 7, 'e_m': 0.024091, 'e_o_k': [0.021079, 0.012648], 'p_i': 10, 'u_i': 1.4858},
    ]
    B_BUDGET = 88.320015
    return processors, tasks, B_BUDGET
