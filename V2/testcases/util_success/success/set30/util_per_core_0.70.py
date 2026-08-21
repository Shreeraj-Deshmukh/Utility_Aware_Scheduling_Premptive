"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.281152, 'e_o_k': [0.130198, 0.104159, 0.083327, 0.066662], 'p_i': 10, 'u_i': 2.7000},
        {'id': 1, 'e_m': 0.615508, 'e_o_k': [0.062552, 0.050041, 0.040033, 0.032026], 'p_i': 20, 'u_i': 2.7208},
        {'id': 2, 'e_m': 2.728882, 'e_o_k': [0.277325, 0.221860, 0.177488, 0.141991], 'p_i': 40, 'u_i': 2.5904},
        {'id': 3, 'e_m': 17.032486, 'e_o_k': [2.094158, 1.675326, 1.340261], 'p_i': 80, 'u_i': 1.1735},
        {'id': 4, 'e_m': 9.168777, 'e_o_k': [1.127309, 0.901847, 0.721478], 'p_i': 20, 'u_i': 1.5807},
        {'id': 5, 'e_m': 5.677122, 'e_o_k': [0.576943, 0.461555, 0.369244, 0.295395], 'p_i': 20, 'u_i': 3.3041},
        {'id': 6, 'e_m': 0.229205, 'e_o_k': [0.020455, 0.016364, 0.013091, 0.010473, 0.008378], 'p_i': 10, 'u_i': 2.4289},
        {'id': 7, 'e_m': 7.790633, 'e_o_k': [0.957865, 0.766292, 0.613033], 'p_i': 40, 'u_i': 4.0306},
    ]
    B_BUDGET = 167.440001
    return processors, tasks, B_BUDGET
