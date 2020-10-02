# Deploy trained model with TensorFlow Serving and Docker

Deploy a cat and dog detector with the help of TensorFlow Serving and Docker

## Requirements

Run the following command to install the necessary dependencies on your system:

```bash
pip3 install -r requirements.txt
```

## Usage

1. Run Docker container to serve model

```bash
docker run -p 8501:8501 --name=dog-cat-detector -v "path/to/model/folder:/models/pets/1" -e MODEL_NAME=pets tensorflow/serving
```

2. Run the web server

```bash
python3 app.py
```

3. Open the web browser and navigate to the URL `http://localhost:5000` to see the result.
