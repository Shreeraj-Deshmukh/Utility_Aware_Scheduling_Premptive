"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.396763, 'e_o_k': [0.081304, 0.065043, 0.052034], 'p_i': 10, 'u_i': 3.3143},
        {'id': 1, 'e_m': 0.524964, 'e_o_k': [0.107575, 0.086060, 0.068848], 'p_i': 20, 'u_i': 3.2246},
        {'id': 2, 'e_m': 3.768792, 'e_o_k': [0.772294, 0.617835, 0.494268], 'p_i': 40, 'u_i': 4.6504},
        {'id': 3, 'e_m': 8.561063, 'e_o_k': [1.754316, 1.403453, 1.122762], 'p_i': 80, 'u_i': 4.9346},
        {'id': 4, 'e_m': 0.427036, 'e_o_k': [0.087507, 0.070006, 0.056005], 'p_i': 10, 'u_i': 2.0105},
        {'id': 5, 'e_m': 1.656317, 'e_o_k': [0.339409, 0.271527, 0.217222], 'p_i': 40, 'u_i': 3.0068},
        {'id': 6, 'e_m': 0.919393, 'e_o_k': [0.188400, 0.150720, 0.120576], 'p_i': 80, 'u_i': 1.6248},
        {'id': 7, 'e_m': 2.979082, 'e_o_k': [0.610468, 0.488374, 0.390699], 'p_i': 80, 'u_i': 2.1190},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
