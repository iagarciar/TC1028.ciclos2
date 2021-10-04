# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["5","2","4","6","8","10"],
        ["","","","","","", "[2, 4, 6, 8, 10]","[4, 16, 36, 64, 100]"],
        "Error en una de las 2 listas o en los números dentro de ellas"
    ),
    # Test case 2
    (
        ["0"],
        ["", "[]","[]"],
        "¿Las listas estan vacias si la entrada es 0?"
    ),
# Test case 3
 (
        ["3","2","4","6"],
        ["","","","", "[2, 4, 6]","[4, 16, 36]"],
        "Error en una de las 2 listas o en los números dentro de ellas"
),
# Test case 4
(
        ["5","1","1","1","1","1"],
        ["","","","","","", "[1, 1, 1, 1, 1]","[1, 1, 1, 1, 1]"],
        "Error en una de las 2 listas o en los números dentro de ellas"
),
# Test case 5
(
        ["2","0","100"],
        ["","","", "[0, 100]","[0, 10000]"],
        "Error en una de las 2 listas o en los números dentro de ellas"
)
]
