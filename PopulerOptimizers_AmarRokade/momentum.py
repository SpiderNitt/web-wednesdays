from numpy import zeros
def update_params_with_momentum(params, grads, v, beta, learning_rate):
    
    # grads has the dw and db parameters from backprop
    # params  has the W and b parameters which we have to update 
    for l in range(len(params) // 2 ):
        # HERE WE COMPUTING THE VELOCITIES 
        v["dW" + str(l)] = beta * v["dW" + str(l)] + (1 - beta) * grads['dW' + str(l)]
        v["db" + str(l)] = beta * v["db" + str(l)] + (1 - beta) * grads['db' + str(l)]
        
        #updating parameters W and b
        params["W" + str(l)] = params["W" + str(l)] - learning_rate * v["dW" + str(l)]
        params["b" + str(l)] = params["b" + str(l)] - learning_rate * v["db" + str(l)]
    return params


def initilization_moment(params):
    v = {}
    for i in range(len(params)//2 ):
        v["dW" + str(i)] = zeros(params["W" + str(i)].shape)
        v["db" + str(i)] = zeros(params["b" + str(i)].shape)
    return v
