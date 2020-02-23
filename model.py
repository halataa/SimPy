from tensorflow import keras as k
import numpy as np

INPUT_SHAPE = (7,10,1)
#Input Layer

input_layer = k.layers.Input(name='the_input',shape=INPUT_SHAPE, dtype = 'float32') #(None,7,10,1)

#Conv Layer

conv1 = k.layers.Conv2D(64,(2,2),name='conv1',activation='relu',padding='same',kernel_initializer='he_normal')(input_layer)
#pool1 = k.layers.MaxPooling1D(pool_size = 2)(conv1)

conv2 = k.layers.Conv2D(64,(2,2),name='conv2',activation='relu',padding='same',kernel_initializer='he_normal')(conv1)
#pool2 = k.layers.MaxPooling1D(pool_size = 2)(conv2)

conv3 = k.layers.Conv2D(64,(2,2),name='conv3',activation='relu',padding='same',kernel_initializer='he_normal')(conv2)
#pool3 = k.layers.MaxPooling1D(pool_size = 2)(conv3)

conv4 = k.layers.Conv2D(64,(2,2),name='conv4',activation='relu',padding='same',kernel_initializer='he_normal')(conv3)
#pool4 = k.layers.MaxPooling1D(pool_size = 2)(conv4)

#CNN to RNN

resshaped = k.layers.Reshape(target_shape = (64,70))(conv4)
dense1 = k.layers.Dense(100)(resshaped)

#LSTM Layer

blstm1 = k.layers.Bidirectional(k.layers.LSTM(64,return_sequences=True,kernel_initializer='he_normal',name='blstm1'))(dense1)

#Flatten

flatten = k.layers.Flatten()(blstm1)

#Output Layer

output_layer = k.layers.Dense(1)(flatten)

#Model

model = k.Model(inputs=input_layer,outputs=output_layer)


