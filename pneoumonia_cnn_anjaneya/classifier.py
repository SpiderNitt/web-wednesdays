from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
import matplotlib.pyplot as plt

train_path = './chest_xray/train'
test_path = './chest_xray/test'
validation_path = './chest_xray/val'

classifier = Sequential()

classifier.add(Conv2D(32, (3, 3), activation = 'relu', input_shape = (64, 64, 1)))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Conv2D(64, (3, 3), activation="relu"))

classifier.add(Conv2D(64, (3, 3), activation="relu"))

classifier.add(Flatten())
classifier.add(Dense(64, activation = 'relu'))
classifier.add(Dropout(0.2))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer = 'adam' ,loss = 'binary_crossentropy', metrics = ['accuracy'])

classifier.summary()

image_datagen = ImageDataGenerator(
        rescale = 1./255,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True)

train_generator = image_datagen.flow_from_directory(
        train_path,
        target_size = (64, 64),
        color_mode = 'grayscale',
        batch_size = 1,
        class_mode = 'binary')

validation_generator = image_datagen.flow_from_directory(
        validation_path,
        target_size = (64, 64),
        color_mode = 'grayscale',
        batch_size = 1,
        class_mode = 'binary')

test_generator = image_datagen.flow_from_directory(
        test_path,
        target_size = (64, 64),
        color_mode = 'grayscale',
        batch_size = 1,
        class_mode = 'binary')

print('\nTraining Started...')

history = classifier.fit(
        train_generator,
        steps_per_epoch = 50,
        epochs = 150,
        validation_data = validation_generator,
        validation_steps = 100)

print('\nEvaluating on test set...')

classifier.evaluate(test_generator)

# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()






















