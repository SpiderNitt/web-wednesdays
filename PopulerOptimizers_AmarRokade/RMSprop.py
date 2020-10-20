import numpy as  np

def initilization_RMS(params):
    s = {}
    for i in range(len(params)//2 ):
        s["dW" + str(i)] = np.zeros(params["W" + str(i)].shape)
        s["db" + str(i)] = np.zeros(params["b" + str(i)].shape)
    return s

def update_params_with_RMS(params, grads,s, beta, learning_rate):
    
    # grads has the dw and db parameters from backprop
    # params  has the W and b parameters which we have to update 
    for l in range(len(params) // 2 ):
        # HERE WE COMPUTING THE VELOCITIES 
        s["dW" + str(l)]= beta * s["dW" + str(l)] + (1 - beta) * np.square(grads['dW' + str(l)])
        s["db" + str(l)] = beta * s["db" + str(l)] + (1 - beta) * np.square(grads['db' + str(l)])
        
        #updating parameters W and b
        params["W" + str(l)] = params["W" + str(l)] - learning_rate * grads['dW' + str(l)] / (np.sqrt( s["dW" + str(l)] )+ pow(10,-4))
        params["b" + str(l)] = params["b" + str(l)] - learning_rate * grads['db' + str(l)] / (np.sqrt( s["db" + str(l)]) + pow(10,-4))

    return params


