# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["5","4","3","/","3","2","4","/","*"],
        ["","","","","","","","","", "[8, 6, 7]"],
        "Respuesta incorrecta"
    ),
    #Test case 2
    (
        ["3","2","/","2","3","/","*"],
        ["","","","","","","", "[5, 5]"],
        "Respuesta incorrecta"
    ),
    #Test case 3
    (
        ["1","1","1","1","/","0","0","0","0","/","*"],
        ["","","","","","","","","","","", "[1, 1, 1, 1]"],
        "Respuesta incorrecta"
    )
]
