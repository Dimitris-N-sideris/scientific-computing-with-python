from pytest import main


def arithmetic_arranger(problems, display=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    line1 = ""
    line2 = ""
    dottedline = ""
    resultline = ""
    leastSpaceBetweenProblems = " " * 4
    newline = "\n"
    for equation in problems:
        splitted = equation.split(" ")
        if len(splitted) < 3:
            return "Error: Operator must be '+' or '-'"
        try:
            result = errorCheck(splitted[0], splitted[2], splitted[1])
        except Exception as inst:
            return inst.args[0]
        lineWidth = len(str(max([int(splitted[0]), int(splitted[2])]))) + 2
        if line1 != "":
            line1 += leastSpaceBetweenProblems
            line2 += leastSpaceBetweenProblems
            dottedline += leastSpaceBetweenProblems
            resultline += leastSpaceBetweenProblems
        line1 += ((lineWidth - len(splitted[0])) * " ") + splitted[0]
        line2 += splitted[1] + ((lineWidth - len(splitted[2]) - 1) * " ") + splitted[2]
        resultline += ((lineWidth - len(str(result))) * " ") + str(result)
        dottedline += "-" * lineWidth

    if display:
        return line1 + newline + line2 + newline + dottedline + newline + resultline
    return line1 + newline + line2 + newline + dottedline


def errorCheck(variable1, variable2, symbol):
    result = ""
    if not (symbol == "+" or symbol == "-"):
        raise Exception("Error: Operator must be '+' or '-'.")
    try:

        if symbol == "+":
            result = int(variable1) + int(variable2)

        if symbol == "-":
            result = int(variable1) - int(variable2)

        if int(variable1) > 9999 or int(variable2) > 9999:
            raise Exception("Error: Numbers cannot be more than four digits.")

    except ValueError:
        raise Exception("Error: Numbers must only contain digits.")

    return result


main()
