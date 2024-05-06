from application_service.HomeStateServiceImpl import HomeStateServiceImpl
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/home', methods=['GET'])
def get_home_state():
    try:
        states = HomeStateServiceImpl.retrieve_home_state(request.args.get('present'), request.args.get('occupied'))

        if states:
            return jsonify(states)
        else:
            raise Exception("Not Found")
    except Exception as e:
        return jsonify({"message":e.args}), 400


@app.route('/api/home', methods=['PUT'])
def update_home_state():
    try:
        home_state_by_id = HomeStateServiceImpl.update(request.get_json())
        return jsonify(home_state_by_id)
    except Exception as e:
        return jsonify({"message": e.args}), 404

if __name__ == '__main__':
    app.run(debug=True)

