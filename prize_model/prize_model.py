#compute any possible equilibriums given a value and a step by which to increment available prices from 0
#output will only give one permuation for each equilibrium for the sake of efficiency
#usage: for prices $0, 15, 30 and value of 30 run: prize_model(30,15)

def prize_model(value, step):

    #empty list to add equilibrium to
    l = []


    # loop through each choice (loops do not repeat non-unique combinations)

    for i in range(0, value + 1, step):
        for j in range(i, value + 1, step):
            for k in range(j, value + 1, step):

                # calculate payoff for each

                (x, y, z) = compute_ex_value(i,j,k, value)

                #booleans for if x, y, z are best responding. Assume they are, switch to false if they arent
                x_eq = True
                y_eq = True
                z_eq = True

                #check if best response for each, conditioned on other two variables
                #if not best response

                #check if player one is best responding

                for alt_i in range(0, value+1, step):
                    if (alt_i != i):
                        (x_1, y_1, z_1) = compute_ex_value(alt_i,j,k, value)
                        if x_1 > x:
                            x_eq = False
                            break

                # if they are, check if player two is also best responding
                if (x_eq == True):
                    for alt_j in range(0, value+1, step):


                        if (alt_j != j):
                            (x_1, y_1, z_1) = compute_ex_value(i, alt_j, k, value)
                            if y_1 > y:
                                y_eq = False
                                break;

                # if they both are, check if player three is also best responding
                if (y_eq == True):
                    for alt_k in range(0, value+1, step):

                        if (alt_k != k):
                            (x_1, y_1, z_1) = compute_ex_value(i, j, alt_k, value)

                            if z_1 > z:
                                z_eq = False
                                break

            #if all player are best responding, then append this combination to the list (it is an equilibrium)
                if (x_eq and y_eq and z_eq):
                    l.append([i, j, k])

    return l










#helper function to compute payoffs

def compute_ex_value(i, j, k, value):

    m = max(i, j, k)
    i_value = -i
    j_value = -j
    k_value = -k

    #if all variables are 0, payoffs are all zero
    if (i == j == k == 0):
        i_value = 0
        j_value = 0
        k_value = 0

    #all payoffs are equal and non-zero
    elif (i == m and j == m and k == m):
        i_value += value / 3.0
        j_value += value / 3.0
        k_value += value / 3.0

    #other cases...
    elif (i == m and j == m):
        i_value += value / 2.0
        j_value += value / 2.0

    elif (j == m and k == m):
        k_value += value / 2.0
        j_value += value / 2.0

    elif (i == m and k == m):
        k_value += value / 2.0
        i_value += value / 2.0

    elif (i == m):
        i_value += value

    elif (j == m):
        j_value += value

    elif (k == m):
        k_value += value


    #return payoffs
    return (i_value, j_value, k_value)




#test cases
print("equilibriums for value 30, step 15: " + str(prize_model(30, 15)))
print("equilibriums for value 100, step 25: " + str(prize_model(100, 25)))
print("equilibriums for value 100, step 50: " + str(prize_model(100, 50)))
print("equilibriums for value 3, step 1: " + str(prize_model(3, 1)))
