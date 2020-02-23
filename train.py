from tensorflow import keras as k
from model import model
from data_gen import data_gen
import os
import jdatetime

train_dir = 'data\\dataset\\train.csv'
test_dir = 'data\\dataset\\test.csv'
BATCH_SIZE = 64
EPOCHS = 20

train_gen = data_gen(train_dir, BATCH_SIZE)
val_gen = data_gen(test_dir, BATCH_SIZE)
train_gen.build_data()
val_gen.build_data()

now = jdatetime.datetime.today()

model_folder_name = '%s-%s[%s-%s]__Model' % (
    now.month, now.day, now.hour, now.minute)
os.mkdir('data\\models\\%s' % model_folder_name)

tensorboard_callback = k.callbacks.TensorBoard(
    log_dir='data\\models\\%s'%(model_folder_name), histogram_freq=1)

adam = k.optimizers.Adam()
model.compile(loss='mean_squared_error', optimizer=adam)

history = model.fit_generator(generator=train_gen.next_batch(),
                    steps_per_epoch=int(train_gen.n / train_gen.batch_size),
                    epochs=EPOCHS,
                    validation_data=val_gen.next_batch(),
                    validation_steps=int(val_gen.n / val_gen.batch_size),verbose=1,callbacks=[tensorboard_callback])

model.save_weights('data\\models\\%s\\model.h5'%model_folder_name)