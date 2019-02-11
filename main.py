import flask
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

clip_size = 200

model = load_model('sentiment_analyser.h5')
model._make_predict_function()
graph = tf.get_default_graph()

app = flask.Flask(__name__)


@app.route("/analyze", methods=["GET"])
def predict():
	params = flask.request.json['text']

	tokenized = tokenizer.texts_to_sequences([params])
	seq = pad_sequences(tokenized, maxlen=clip_size)

	print(params)
	with graph.as_default():	
		data = {"score": float(model.predict([seq])[0][0])}


	return flask.jsonify(data)

@app.route("/", methods=['GET'])
def kek():
	print("OK")
	return flask.jsonify({"score": "OK"})

