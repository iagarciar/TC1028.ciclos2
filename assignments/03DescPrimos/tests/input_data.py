# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
        #Inputs
        ["101"],
        # Ouputs
        ["", "101"],
        # Message in case of failure
        ["El número que se ingreso es un número primo, por lo cual la salida solo debería ser un factor primo"]
    ),
    # Test case 2
    (
        #Inputs
        ["9999999"],
        # Ouputs
        ["", "3","3","239","4649"],
        # Message in case of failure
        ["Tienes los dos 3"]
    ),
    # Test case 3
    (
        #Inputs
        ["1000"],
        # Ouputs
        ["", "2","2","2","5","5","5"],
        # Message in case of failure
        ["En algunas ocasiones un factor primo se puede repetirse tres o más veces"]
    ),
    # Test case 4
    (
        #Inputs
        ["4000"],
        # Ouputs
        ["", "2","2","2","2","2","5","5","5"],
        # Message in case of failure
        ["En algunas ocasiones un factor primo se puede repetirse tres o más veces"]
    )
    
]
