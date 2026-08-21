"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.548867, 'e_o_k': [0.260303, 0.208242, 0.166594, 0.133275], 'p_i': 10, 'u_i': 2.8575},
        {'id': 1, 'e_m': 2.063126, 'e_o_k': [0.859227, 0.687381, 0.549905, 0.439924, 0.351939], 'p_i': 20, 'u_i': 2.8209},
        {'id': 2, 'e_m': 0.270075, 'e_o_k': [0.210058, 0.168047], 'p_i': 40, 'u_i': 2.9332},
        {'id': 3, 'e_m': 4.026670, 'e_o_k': [2.310384, 1.848307, 1.478646], 'p_i': 80, 'u_i': 1.0372},
        {'id': 4, 'e_m': 4.012113, 'e_o_k': [2.302032, 1.841626, 1.473301], 'p_i': 10, 'u_i': 1.7921},
        {'id': 5, 'e_m': 7.346417, 'e_o_k': [2.787802, 2.230242, 1.784194, 1.427355, 1.141884, 0.913507], 'p_i': 40, 'u_i': 1.1296},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
