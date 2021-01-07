from flask import Flask, jsonify, stream_with_context, Response, request
from flask_socketio import send, emit, SocketIO
import solver

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def hello():
    html = "<h3>Hello, World!</h3>"
    return html

@app.route("/evolve")
def evolve():
	pop_size = int(request.args.get('pop_size'))
	n = int(request.args.get('n'))
	return Response(stream_with_context(solver.evolution(pop_size, n)))

if __name__ == "__main__":
  socketio.run(app, host='0.0.0.0', port=8023)
  # app.run(host='0.0.0.0', port=80)