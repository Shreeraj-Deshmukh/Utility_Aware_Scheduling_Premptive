"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120005, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120005, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.435307, 'e_o_k': [0.422374, 0.337899, 0.270319], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 3.359917, 'e_o_k': [0.559986, 0.447989], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 16.985731, 'e_o_k': [1.726192, 1.380954, 1.104763, 0.883810], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 22.257501, 'e_o_k': [3.709584, 2.967667], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 2.040729, 'e_o_k': [0.182121, 0.145697, 0.116558, 0.093246, 0.074597], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 17.867967, 'e_o_k': [1.452964, 1.162371, 0.929897, 0.743917, 0.595134, 0.476107], 'p_i': 40, 'u_i': 3.0218},
        {'id': 6, 'e_m': 2.079410, 'e_o_k': [0.185573, 0.148459, 0.118767, 0.095014, 0.076011], 'p_i': 20, 'u_i': 2.6468},
        {'id': 7, 'e_m': 30.713881, 'e_o_k': [2.497551, 1.998041, 1.598433, 1.278746, 1.022997, 0.818397], 'p_i': 80, 'u_i': 1.1768},
    ]
    B_BUDGET = 263.120005
    return processors, tasks, B_BUDGET
