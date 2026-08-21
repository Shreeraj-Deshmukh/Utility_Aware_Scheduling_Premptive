"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.230439, 'e_o_k': [0.064011, 0.051209], 'p_i': 10, 'u_i': 4.4014},
        {'id': 1, 'e_m': 1.720704, 'e_o_k': [0.477973, 0.382379], 'p_i': 20, 'u_i': 2.2645},
        {'id': 2, 'e_m': 4.747157, 'e_o_k': [1.318655, 1.054924], 'p_i': 40, 'u_i': 4.9290},
        {'id': 3, 'e_m': 5.488993, 'e_o_k': [1.524720, 1.219776], 'p_i': 80, 'u_i': 2.8289},
        {'id': 4, 'e_m': 2.627935, 'e_o_k': [0.729982, 0.583986], 'p_i': 20, 'u_i': 2.4039},
        {'id': 5, 'e_m': 2.026805, 'e_o_k': [0.563001, 0.450401], 'p_i': 10, 'u_i': 2.7593},
        {'id': 6, 'e_m': 12.325637, 'e_o_k': [3.423788, 2.739030], 'p_i': 80, 'u_i': 4.9185},
        {'id': 7, 'e_m': 1.238545, 'e_o_k': [0.344040, 0.275232], 'p_i': 80, 'u_i': 1.9966},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
