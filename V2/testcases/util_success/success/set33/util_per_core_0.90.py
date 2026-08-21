"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279998, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279998, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.397066, 'e_o_k': [0.566178, 0.452942], 'p_i': 10, 'u_i': 3.5122},
        {'id': 1, 'e_m': 4.365317, 'e_o_k': [0.354973, 0.283978, 0.227183, 0.181746, 0.145397, 0.116318], 'p_i': 20, 'u_i': 2.8569},
        {'id': 2, 'e_m': 8.849197, 'e_o_k': [1.474866, 1.179893], 'p_i': 40, 'u_i': 4.3008},
        {'id': 3, 'e_m': 4.516221, 'e_o_k': [0.458966, 0.367172, 0.293738, 0.234990], 'p_i': 80, 'u_i': 2.2362},
        {'id': 4, 'e_m': 4.363979, 'e_o_k': [0.443494, 0.354795, 0.283836, 0.227069], 'p_i': 10, 'u_i': 3.7312},
        {'id': 5, 'e_m': 0.941816, 'e_o_k': [0.095713, 0.076570, 0.061256, 0.049005], 'p_i': 20, 'u_i': 3.2074},
        {'id': 6, 'e_m': 12.648135, 'e_o_k': [1.128760, 0.903008, 0.722407, 0.577925, 0.462340], 'p_i': 80, 'u_i': 3.9809},
        {'id': 7, 'e_m': 25.820357, 'e_o_k': [4.303393, 3.442714], 'p_i': 80, 'u_i': 1.3445},
    ]
    B_BUDGET = 215.279998
    return processors, tasks, B_BUDGET
