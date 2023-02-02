import tensorflow as tf
import numpy as np
import tensorflow.keras.backend as K
import t3f

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import optimizers

class Learner:
  def __init__(self):
    initializer = t3f.glorot_initializer([[4, 7, 4, 7], [5, 5, 5, 5]], tt_rank=2)
    self.W1 = t3f.get_variable('W1', initializer=initializer)
    self.W2 = tf.Variable(tf.random.normal([625, 10]))
    self.b2 = tf.Variable(tf.random.normal([10]))

  def predict(self, x):
    b1 = tf.Variable(tf.zeros([625]))
    h1 = t3f.matmul(x, W1) + b1
    h1 = tf.nn.relu(h1)
    return tf.matmul(h1, W2) + b2

  def loss(self, x, y):
    y_ = tf.one_hot(y, 10)
    logits = self.predict(x)
    return tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=logits))


# Fix seed so that the results are reproducable.
tf.random.set_seed(0)
np.random.seed(0)

W = t3f.random_matrix([[4, 7, 4, 7], [5, 5, 5, 5]], tt_rank=2)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# preprocessing

x_train = x_train / 127.5 - 1.0
x_test = x_test / 127.5 - 1.0

y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
tt_layer = t3f.nn.KerasDense(input_dims=[7, 4, 7, 4], output_dims=[5, 5, 5, 5],
                             tt_rank=4, activation='relu',
                             bias_initializer=1e-3)
model.add(tt_layer)
model.add(Dense(10))
model.add(Activation('softmax'))

print('\n\n\n\n\n', model.summary())
optimizer = optimizers.Adam(lr=1e-2)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
print('\n\n\n\n\n', model.fit(x_train, y_train, epochs=3, batch_size=64, validation_data=(x_test, y_test)))

# Compression of Dense layers
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(625, activation='relu'))
model.add(Dense(10))
model.add(Activation('softmax'))
print('\n\n\n\n\n', model.summary())

optimizer = optimizers.Adam(lr=1e-3)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
print('\n\n\n\n\n', model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test)))
      
W = model.trainable_weights[0]
print(W)
Wtt = t3f.to_tt_matrix(W, shape=[[7, 4, 7, 4], [5, 5, 5, 5]], max_tt_rank=16)
print(Wtt)

cores = Wtt.tt_cores
other_params = model.get_weights()[1:]

model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
tt_layer = t3f.nn.KerasDense(input_dims=[7, 4, 7, 4], output_dims=[5, 5, 5, 5],
                             tt_rank=16, activation='relu')
model.add(tt_layer)
model.add(Dense(10))
model.add(Activation('softmax'))

optimizer = optimizers.Adam(lr=1e-3)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

model.set_weights(list(cores) + other_params)

print("\n\n", "new accuracy: ", model.evaluate(x_test, y_test)[1])

print('\n\n\n\n\n', model.summary())

print('\n\n\n\n\n', model.fit(x_train, y_train, epochs=2, batch_size=64, validation_data=(x_test, y_test)))
model.save('model9')
