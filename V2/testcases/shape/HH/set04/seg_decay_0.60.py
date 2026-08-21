"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.929756, 'e_o_k': [0.546144, 0.327687, 0.196612, 0.117967, 0.070780, 0.042468], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.056878, 'e_o_k': [0.033410, 0.020046, 0.012028, 0.007217, 0.004330, 0.002598], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 2.623994, 'e_o_k': [2.295995, 1.377597], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 4.474673, 'e_o_k': [3.915339, 2.349203], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 2.349668, 'e_o_k': [2.055960, 1.233576], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 10.542988, 'e_o_k': [6.783173, 4.069904, 2.441942, 1.465165], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.342456, 'e_o_k': [0.299649, 0.179789], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 3.346871, 'e_o_k': [2.928512, 1.757107], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET
