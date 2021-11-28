def sort_sentence(sentence):
#I didn't really understand how to make it more "complicated", sorry <3
    parallel = []
    for index, face in enumerate(sentence.split()):
        parallel.append((len(face), index, face.lower()))

#making the sentence start with the capital letter, just like in the example
    heart = [face[2] for face in sorted(parallel)]
    heart[0] = heart[0][0].upper() + heart[0][1:]
    return " ".join(heart)
#here it is!

