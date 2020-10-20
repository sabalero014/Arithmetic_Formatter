def arithmetic_arranger(problems, op_par=False):
    first = ""
    second = ""
    answer = ""
    line = "-"
    lines = ''

    # ERROR #
    # TOO MANY PROBLEMS (LIMIT IS 5)
    if len(problems) >= 6:
        return 'Error: Too many problems.'

    for i in problems:
        operation = i.split()
        first_number = operation[0]
        operator_digit = operation[1]
        second_number = operation[2]

        # ERROR #
        # NUMBER HAS MORE THAN 4 DIGITS
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        # ERROR #
        # NUMBER CONTAINS A LETTER CHARACTER
        if not first_number.isnumeric() or not second_number.isnumeric():
            return "Error: Numbers must only contain digits."

        # ERROR #
        # OPERATOR IS '/' OR '*'
        if operator_digit == '+' or operator_digit == '-':
            if operator_digit == '+':
                result = str(int(first_number) + int(second_number))
            else:
                result = str(int(first_number) - int(second_number))

            length = max(len(first_number), len(second_number)) + 2
            top_line = first_number.rjust(length)
            bottom_line = operator_digit + second_number.rjust(length - 1)
            result_line = result.rjust(length)

            if i != problems[-1]:
                first += top_line + '    '
                second += bottom_line + '    '
                lines += line*length + '    '
                answer += result_line + '    '

            else:
                first += top_line
                second += bottom_line
                lines += line * length
                answer += result_line

        else:
            return "Error: Operator must be '+' or '-'."

    first.rstrip()
    second.rstrip()
    lines.rstrip()

    if op_par:
        arranged_problems = first + "\n" + second + "\n" + lines + "\n" + answer

    else:
        arranged_problems = first + "\n" + second + "\n" + lines

    return arranged_problems

