# char-embeddings on Google ML Engine
![](char-tsne-embed.png)

[char-embeddings](https://github.com/minimaxir/char-embeddings) is a repository by [Max Woolf](https://github.com/minimaxir) containing 300D character embeddings derived from the GloVe 840B/300D dataset, and uses these embeddings to train a deep learning model to generate text using [Keras](https://keras.io/). The generation and model construction is heavily modified after the [automatic text generation](https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py) Keras example by [François Chollet](https://twitter.com/fchollet). This repository takes this work, makes it generic, and refactors it to run on Google's ML Engine with sensible environment variables and an example script to execute training on a GPU instance.

## Usage

This repository contains a number of Python 3 scripts:

- `create_embeddings.py`: Converts a pretrained word embeddings file into a character embeddings file by averaging the per-character vectors.
- `text_generator_keras.py`: Constructs and trains the Keras model, producing some text at each epoch.
- `text_generator_keras_sample.py`: Using the text file and Keras model generated from the previous two scripts, generate text.

The `output` folder contains text output at each epoch, a log of losses at every 50th batch, the learned character embeddings at the last epoch, the trained model itself, and a sample of generated text.

## Requirements
keras, tensorflow, h5py, scikit-learn

## License
MIT
