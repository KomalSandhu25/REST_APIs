home_states_by_id = {
    "ID1": {"ID": "ID1", "State": "Home", "Occupied": "Y", "Present": "Y"},
    "ID2": {"ID": "ID2", "State": "Away", "Occupied": "N", "Present": "N"},
    "ID3": {"ID": "ID3", "State": "Sleep", "Occupied": "N", "Present": "Y"}
}

home_states_by_occupancy = {
    "Y": ["ID1"],
    "N": ["ID2", "ID3"]
}

home_states_by_presence = {
    "Y": ["ID1", "ID3"],
    "N": ["ID2"]
}