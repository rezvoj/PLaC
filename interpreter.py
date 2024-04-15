import sys



def loadProgram():
    if len(sys.argv) < 2:
        print("Error: Program file not specified")
        exit(0)
    labels, instructions = list(), list()
    try:
        with open(sys.argv[1]) as inputFile:
            for idx, line in enumerate(inputFile):
                line = line.strip()
                parameters = line.split(" ", maxsplit=2)
                if parameters[0] == "label":
                    labelIdx = int(parameters[1])
                    if labelIdx >= len(labels):
                        labels.extend([0] * (labelIdx + 1 - len(labels)))
                    labels[labelIdx] = idx
                instructions.append(tuple(parameters))
    except:
        print(f"File '{sys.argv[1]}' does not exist")
        exit(0)
    return labels, instructions


class Operations:
    unary = {
        "uminus": lambda a: -a, 
        "not": lambda a: not a, 
        "itof": float
    }
    binary = {
        "add": lambda a, b: a + b, "sub": lambda a, b: a - b, 
        "mul": lambda a, b: a * b, 
        "div": lambda a, b: a // b if type(a) == int else a / b,
        "mod": lambda a, b: a % b, "concat": lambda a, b: a + b,
        "and": lambda a, b: a and b, "or": lambda a, b: a or b,
        "gt": lambda a, b: a > b, "lt": lambda a, b: a < b, 
        "eq": lambda a, b: a == b,
    }


def getValueOfType(typeStr: str, value, rmQuotes = False):
    match typeStr:
        case "int":
            return int(value)
        case "float":
            return float(value)
        case "bool":
            if value == "true":
                return True
            elif value == "false":
                return False
            raise ValueError()
        case "string":
            if rmQuotes:
                return value[1:-1]
            return value
    raise ValueError()


def handleInstruction(stack: list, instruction: tuple):
    if instruction[0] in Operations.unary:
        stack[-1] = Operations.unary[instruction[0]](stack[-1])
    elif instruction[0] in Operations.binary:
        value = stack.pop()
        stack[-1] = Operations.binary[instruction[0]](stack[-1], value)


def main():
    labels, instructions = loadProgram()
    stack, variables = list(), dict()
    instructionIdx = 0
    while instructionIdx < len(instructions):
        match instructions[instructionIdx][0]:
            case "push":
                parameters = instructions[instructionIdx]
                stack.append(getValueOfType(parameters[1], parameters[2], True))
            case "pop":
                stack.pop()
            case "load":
                variableName = instructions[instructionIdx][1]
                stack.append(variables[variableName])
            case "save":
                variableName = instructions[instructionIdx][1]            
                variables[variableName] = stack.pop()
            case "jmp":
                labelId = int(instructions[instructionIdx][1])
                instructionIdx = labels[labelId]
            case "fjmp":
                if not stack[-1]:
                    instructionIdx = labels[int(instructions[instructionIdx][1])]
                stack.pop()
            case "print":
                count = int(instructions[instructionIdx][1])
                for _ in range(count):
                    value = stack.pop()
                    if type(value) == bool:
                        value = str(value).lower()
                    if type(value) == float:
                        value = round(value, 6)
                    print(value, end="")
                print()
            case "read":
                try:
                    stack.append(getValueOfType(instructions[instructionIdx][1], input()))
                except:
                    print("Error: Invalid type", file=sys.stderr)  
                    exit(0)
            case _:
                handleInstruction(stack, instructions[instructionIdx])
        instructionIdx += 1


if __name__ == '__main__':
    main()
