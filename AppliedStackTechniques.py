
import ArrayStack


def reverse_file(filename: str) -> object:
    """

    :param filename: a file and or its path
    :return: line-by-line new file reverse
    """
    stack = ArrayStack.ArrayStack()
    fp = open(filename)
    for line in fp.readlines():
        stack.push(line.rstrip('\n'))
    fp.close()

    output = open("reverse_" + filename, "w")

    print(stack.isEmpty())
    while not stack.isEmpty():
        print(stack.isEmpty())
        output.write(stack.pop)
        output.write('\n')
    output.close()


def matching_delimiters(expression: str) -> bool:
    """

    :param expression: character matching expresstion
    :return: boolean if matched return True, else return false
    """
    lefty = "({["
    righty = ")}]"
    stack = ArrayStack.ArrayStack()
    for c in expression:
        if c in lefty:
            stack.push(c)
        elif c in righty:
            if stack.isEmpty():
                return False
            elif righty.index(c) != lefty.index(stack.pop):
                return True
    return stack.isEmpty()


def html_matching_delimiters(htmlCode: str) -> bool:
    """
    return true if the html code delimiters and tags is matched.
    :param htmlCode: the String representation of htmlCode
    :return: True if matched, False otherwise
    """
    stack = ArrayStack.ArrayStack()
    firstTag = htmlCode.find("<")
    while firstTag != -1:
        endTag = htmlCode.find(">")
        if endTag == -1:
            return False
        tag = htmlCode[firstTag + 1 : endTag]
        if not tag.startswith("/"):
            stack.push(tag)
        else:
            if stack.isEmpty():
                return False
            if htmlCode[1:] != stack.pop:
                return False
        firstTag = htmlCode.find("<", endTag + 1)
    return stack.isEmpty()

if __name__ == '__main__':
    reverse_file("ds.txt")