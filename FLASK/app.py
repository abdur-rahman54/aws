from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from POST request
        input_data = request.form['input_values']

        # Run docker-model.py as subprocess
        result = subprocess.run(['python', 'docker-model.py', input_data], capture_output=True, text=True)

        # Parse the output
        prediction = result.stdout.strip()

        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

