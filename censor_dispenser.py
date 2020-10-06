# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def work_with_text(text):
    new_text = text.lower()
    new_text = new_text.split()
    new_text_two = []
    for i in new_text:
        new_i = i.strip(',.!()\"')
        new_text_two.append(new_i)
    return new_text_two


# print(work_with_text(email_three))

def censoring(text, phrase):
    new_text = text.replace(phrase, "@@@@")
    return new_text


# print(censoring(email_one,"learning algorithms"))

def censoring_two(text, terms):
    new_text = text
    for i in terms:
        new_text = new_text.replace(i, "&&&")
    return new_text


def censoring_three(text, terms, words):
    new_text = censoring_two(text, terms)
    count = 0
    yes = 0
    new_text_two = work_with_text(new_text)
    new_text_three = []
    for word in new_text_two:
        for i in words:
            yes = 0
            if (i == word):
                count += 1
                if (count > 2):
                    yes += 1
                    new_text_three.append("%%%")
                    break

        if (yes == 0):
            new_text_three.append(word)
    # result = " ".join(new_text_three)
    return new_text_three


def censoring_four(text, terms, words):
    new_text = censoring_three(text, terms, words)
    count = 0
    for i in range(len(new_text)):
        if (new_text[i] == "&&&") or (new_text[i] == "%%%"):
            count += 1
            new_text[i - 1] = "!!!"
            new_text[i + 1] = "!!!"
    return new_text


# print(censer_four(email_four))


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressing", "concerning", "horrible", "horribly", "questionable"]
# print(censoring_two(email_two,proprietary_terms))

# print(censoring_three(email_three,proprietary_terms,negative_words))

# print(censoring_four(email_four,proprietary_terms,negative_words))
result_four = " ".join(censoring_four(email_four, proprietary_terms, negative_words))
print(result_four)