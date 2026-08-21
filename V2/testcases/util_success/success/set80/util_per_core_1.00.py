"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200014, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200014, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.842906, 'e_o_k': [0.226587, 0.181269, 0.145016], 'p_i': 10, 'u_i': 4.0215},
        {'id': 1, 'e_m': 9.746575, 'e_o_k': [0.869816, 0.695853, 0.556682, 0.445346, 0.356277], 'p_i': 20, 'u_i': 1.4911},
        {'id': 2, 'e_m': 10.223621, 'e_o_k': [1.038986, 0.831189, 0.664951, 0.531961], 'p_i': 40, 'u_i': 3.6858},
        {'id': 3, 'e_m': 13.702903, 'e_o_k': [1.684783, 1.347827, 1.078261], 'p_i': 80, 'u_i': 3.5601},
        {'id': 4, 'e_m': 19.460438, 'e_o_k': [1.582458, 1.265967, 1.012773, 0.810219, 0.648175, 0.518540], 'p_i': 80, 'u_i': 2.9573},
        {'id': 5, 'e_m': 4.634251, 'e_o_k': [0.772375, 0.617900], 'p_i': 40, 'u_i': 4.1230},
        {'id': 6, 'e_m': 11.143482, 'e_o_k': [0.994480, 0.795584, 0.636467, 0.509174, 0.407339], 'p_i': 40, 'u_i': 4.3496},
        {'id': 7, 'e_m': 2.638051, 'e_o_k': [0.214518, 0.171614, 0.137291, 0.109833, 0.087866, 0.070293], 'p_i': 10, 'u_i': 3.3614},
    ]
    B_BUDGET = 239.200014
    return processors, tasks, B_BUDGET
