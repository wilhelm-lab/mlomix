# ToDo: not integrated and needs revision
def get_mod_loss_feature(
    example,
    sequence_column_name,
    feature_column_name="mod_loss",
    default_value=[0, 0, 0, 0, 0, 0],
):
    PTM_LOSS_LOOKUP = {
        "M[UNIMOD:35]": [0, 0, 0, 0, 0, 0],
        "S[UNIMOD:21]": [1, 0, 0, 0, 0, 0],
        "T[UNIMOD:21]": [1, 0, 0, 0, 0, 0],
        "Y[UNIMOD:21]": [1, 0, 0, 0, 0, 0],
        "R[UNIMOD:7]": [1, 0, 1, 0, 0, 0],
        "K[UNIMOD:1]": [1, 0, 0, 0, 0, 0],
        "K[UNIMOD:121]": [1, 0, 0, 0, 0, 0],
        "Q(gl)": [9, 4, 2, 1, 0, 0],
        "R[UNIMOD:34]": [1, 0, 0, 0, 0, 0],
        "K[UNIMOD:34]": [1, 0, 0, 0, 0, 0],
        "T(ga)": [1, 0, 0, 0, 0, 0],
        "S(ga)": [1, 0, 0, 0, 0, 0],
        "T(gl)": [1, 0, 0, 0, 0, 0],
        "S(gl)": [1, 0, 0, 0, 0, 0],
        "C[UNIMOD:4]": [1, 0, 0, 0, 0, 0],
        "[ac]-": [1, 0, 0, 0, 0, 0],
        "E(gl)": [8, 4, 1, 2, 0, 0],
        "K[UNIMOD:36]": [2, 0, 0, 0, 0, 0],
        "K[UNIMOD:37]": [3, 0, 0, 0, 0, 0],
        "K[UNIMOD:122]": [1, 0, 0, 0, 0, 0],
        "K[UNIMOD:58]": [1, 0, 0, 0, 0, 0],
        "K[UNIMOD:1289]": [1, 0, 0, 0, 0, 0],
        "K[UNIMOD:747]": [1, 0, 0, 0, 0, 0],
        "K[UNIMOD:64]": [1, 0, 0, 0, 0, 0],
        "K[UNIMOD:1848]": [1, 0, 0, 0, 0, 0],
        "K[UNIMOD:1363]": [1, 0, 0, 0, 0, 0],
        "K[UNIMOD:1849]": [1, 0, 0, 0, 0, 0],
        "K[UNIMOD:3]": [1, 0, 0, 0, 0, 0],
        "unknown": [3, 0, 2, 0, 0, 0],
        "R[UNIMOD:36]": [2, 0, 0, 0, 0, 0],
        "P[UNIMOD:35]": [1, 0, 0, 0, 0, 0],
        "Y[UNIMOD:354]": [1, 0, 0, 0, 0, 0],
    }
    sequence = example[sequence_column_name].strip("_")

    if "UNIMOD" not in example[sequence_column_name]:
        example[feature_column_name] = [default_value for _ in range(len(sequence))]
        return example

    example[feature_column_name] = [PTM_LOSS_LOOKUP.get(i, [0] * 6) for i in sequence]
    return example


def get_mod_location_feature(
    example,
    sequence_column_name,
    feature_column_name="mod_location",
    default_value=0,
):
    DICT_PTM_MOD_ATOM = {
        "M[UNIMOD:35]": 4,
        "S[UNIMOD:21]": 3,
        "T[UNIMOD:21]": 3,
        "Y[UNIMOD:21]": 3,
        "R[UNIMOD:7]": 1,
        "K[UNIMOD:1]": 2,
        "K[UNIMOD:121]": 2,
        "Q(gl)": 1,
        "R[UNIMOD:34]": 2,
        "K[UNIMOD:34]": 2,
        "T(ga)": 3,
        "S(ga)": 3,
        "T(gl)": 3,
        "S(gl)": 3,
        "C[UNIMOD:4]": 4,
        "[ac]-": 2,
        "E(gl)": 1,
        "K[UNIMOD:36]": 2,
        "K[UNIMOD:37]": 2,
        "K[UNIMOD:122]": 2,
        "K[UNIMOD:58]": 2,
        "K[UNIMOD:1289]": 2,
        "K[UNIMOD:747]": 2,
        "K[UNIMOD:64]": 2,
        "K[UNIMOD:1848]": 2,
        "K[UNIMOD:1363]": 2,
        "K[UNIMOD:1849]": 2,
        "K[UNIMOD:3]": 2,
        "unknown": 1,
        "R[UNIMOD:36]": 2,
        "P[UNIMOD:35]": 1,
        "Y[UNIMOD:354]": 1,
    }

    sequence = example[sequence_column_name].strip("_")

    if "UNIMOD" not in example[sequence_column_name]:
        example[feature_column_name] = [default_value for _ in range(len(sequence))]
        return example

    example[feature_column_name] = [
        DICT_PTM_MOD_ATOM.get(i, default_value) for i in example[sequence_column_name]
    ]
    return example
