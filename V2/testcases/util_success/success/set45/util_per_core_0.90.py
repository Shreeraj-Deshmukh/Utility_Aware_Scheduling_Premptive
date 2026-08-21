"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280014, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280014, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.982688, 'e_o_k': [0.163781, 0.131025], 'p_i': 10, 'u_i': 2.8771},
        {'id': 1, 'e_m': 3.455583, 'e_o_k': [0.351177, 0.280942, 0.224753, 0.179803], 'p_i': 20, 'u_i': 3.3920},
        {'id': 2, 'e_m': 6.199153, 'e_o_k': [1.033192, 0.826554], 'p_i': 40, 'u_i': 1.7352},
        {'id': 3, 'e_m': 17.356137, 'e_o_k': [1.548917, 1.239134, 0.991307, 0.793046, 0.634437], 'p_i': 80, 'u_i': 3.3959},
        {'id': 4, 'e_m': 4.472592, 'e_o_k': [0.549909, 0.439927, 0.351942], 'p_i': 10, 'u_i': 3.3950},
        {'id': 5, 'e_m': 6.902028, 'e_o_k': [0.848610, 0.678888, 0.543110], 'p_i': 40, 'u_i': 1.1151},
        {'id': 6, 'e_m': 7.252381, 'e_o_k': [0.647226, 0.517781, 0.414225, 0.331380, 0.265104], 'p_i': 20, 'u_i': 2.3573},
        {'id': 7, 'e_m': 3.491852, 'e_o_k': [0.429326, 0.343461, 0.274769], 'p_i': 20, 'u_i': 2.0853},
    ]
    B_BUDGET = 215.280014
    return processors, tasks, B_BUDGET
