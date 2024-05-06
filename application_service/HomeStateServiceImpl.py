from secondary_adapter.HomeStateDAO import home_states_by_id, home_states_by_presence, home_states_by_occupancy
from domain.HomeState import HomeState
# Example dictionary to store home states

class HomeStateServiceImpl:

    def retrieve_home_state(present, occupied):
        if present is None or occupied is None:
            raise Exception("Argument present or occupied not found")

        hm_st = HomeState( None, None, present, occupied)

        #id_list_by_occupancy = []
        #id_list_by_presence = []
        states = {}

        if home_states_by_occupancy.__contains__(hm_st.occupied):
            id_list_by_occupancy = home_states_by_occupancy.get(hm_st.occupied)
        else:
            raise Exception("Value for Present not found")

        if home_states_by_presence.__contains__(hm_st.present):
            id_list_by_presence = home_states_by_presence.get(hm_st.present)
        else:
            raise Exception("Value for Occupied not found")

        for it in set(id_list_by_presence).intersection(set(id_list_by_occupancy)):
            states[it] = home_states_by_id.get(it)["State"]
        print(states)
        return states

    def update(home_state):
        if home_state is None:
            raise Exception("Payload is null")
        home_state_obj = HomeState(home_state["id"] if home_state.__contains__("id") else None,
                                   home_state["state"] if home_state.__contains__("state") else None,
                                   home_state["occupied"] if home_state.__contains__("occupied") else None,
                                   home_state["present"] if home_state.__contains__("present") else None)

        if  home_states_by_id.__contains__(home_state_obj.ID):
            home_states_by_id[home_state_obj.ID] = {"ID": home_state_obj.ID,
                                                    "State": home_state_obj.state, "Occupied": home_state_obj.occupied,
                                                    "Present": home_state_obj.present}
        else:
            raise Exception("ID doesn't exist")

        return home_states_by_id