#Desarrollado por Edison Azogue 

import tensorflow as tf
from tensorflow.keras.layers import Conv2D, UpSampling2D, InputLayer
from tensorflow.keras.models import Sequential

def construir_modelo():
    modelo = Sequential()
    modelo.add(InputLayer(input_shape=(32, 32, 1)))
    
    # Codificador
    modelo.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    modelo.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    
    # Decodificador
    modelo.add(UpSampling2D((1, 1)))  # No cambiar las dimensiones
    modelo.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    modelo.add(UpSampling2D((1, 1)))  # No cambiar las dimensiones
    modelo.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    modelo.add(Conv2D(3, (3, 3), activation='sigmoid', padding='same'))
    
    modelo.compile(optimizer='adam', loss='mse')
    
    return modelo