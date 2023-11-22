def shorten(text):
    # text_list = text.split()
    # new_list = "".join([word[0] for word in text.split()])
    # for word in text_list:
    #     new_list.append(word[0])
    return "".join([word[0] for word in text.split()]).upper()


print(shorten('do you know where is bus stop ?'))
