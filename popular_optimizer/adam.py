import numpy as np
def update_params_with_Adam(params, grads,v, s, beta1,beta2, learning_rate,t):
    epsilon = pow(10,-8)    # avoiding to divide to zero
    v_corrected = {}                         
    s_corrected = {} 
    # grads has the dw and db parameters from backprop
    # params  has the W and b parameters which we have to update 
    for l in range(len(params) // 2 ):
        # HERE WE COMPUTING THE VELOCITIES 

        v["dW" + str(l)] = beta1 * v["dW" + str(l)] + (1 - beta1) * grads['dW' + str(l)]
        v["db" + str(l)] = beta1 * v["db" + str(l)] + (1 - beta1) * grads['db' + str(l)]

        v_corrected["dW" + str(l)] = v["dW" + str(l)] / (1 - np.power(beta1, t))
        v_corrected["db" + str(l)] = v["db" + str(l)] / (1 - np.power(beta1, t))


        s["dW" + str(l)] = beta2 * s["dW" + str(l)] + (1 - beta2) * np.power(grads['dW' + str(l)], 2)
        s["db" + str(l)] = beta2 * s["db" + str(l)] + (1 - beta2) * np.power(grads['db' + str(l)], 2)

        s_corrected["dW" + str(l)] = s["dW" + str(l)] / (1 - np.power(beta2, t))
        s_corrected["db" + str(l)] = s["db" + str(l)] / (1 - np.power(beta2, t))

        params["W" + str(l)] = params["W" + str(l)] - learning_rate * v_corrected["dW" + str(l)] / np.sqrt(s_corrected["dW" + str(l)] + epsilon)
        params["b" + str(l)] = params["b" + str(l)] - learning_rate * v_corrected["db" + str(l)] / np.sqrt(s_corrected["db" + str(l)] + epsilon)
    return params

def initilization_Adam(params):
    s = {}
    v = {}
    for i in range(len(params)//2 ):

        v["dW" + str(i)] = np.zeros(params["W" + str(i)].shape)
        v["db" + str(i)] = np.zeros(params["b" + str(i)].shape)

        s["dW" + str(i)] = np.zeros(params["W" + str(i)].shape)
        s["db" + str(i)] = np.zeros(params["b" + str(i)].shape)
    return v, s
