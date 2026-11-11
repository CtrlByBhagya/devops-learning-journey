def comma_code(items):
    if len(items)==1:
        return items[0]

    result=", ".join(items[:-1])+", and "+items[-1]
    return result

spam=['apple','bananas','tofu','cats']

answer=comma_code(spam)
print(answer)