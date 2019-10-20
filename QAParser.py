def parse(filename: str) -> dict:
    """
    Parses Q&A file into Dictionary of stacked lists
    Assembles dictionary where keys are categories and values are lists of lists containing (id, question, answer) triples
    :param filename: file containing questions and answers
    :return: none
    """
    questions = open(filename, "r")

    cats = []
    line = questions.readline()
    if line != "Categories:\n":
        print("\'Categories:\' must be the first line, followed immediately by the categories")

    line = questions.readline()

    while line != "\n":
        cats.append(line[:-1])
        line = questions.readline()

    QAs = dict([(cat, []) for cat in cats])

    while line == "\n":
        line = questions.readline()

    if line[:-2] not in cats:
        print("Error: Invalid Category:", line[:-2], ". Please add it to the top.")

    qid = 0
    while line != "":
        cat = line[:-2]
        line = questions.readline()
        while line[:1] == "\t" or line[:1] == "\n":
            if line[:1] == "\n":
                line = questions.readline()
                continue
            question = line
            answer = questions.readline()
            # print(cat, qid)
            try:
                QAs[cat][qid] = [qid, question[1:-1], answer[1:-1]]
            except IndexError:
                QAs[cat].append([qid, question[1:-1], answer[1:-1]])
            qid += 1

            line = questions.readline()

    questions.close()

    return QAs


def qaoutput(QAs: dict) -> None:
    """Outputting constructed datastructure where the reference is QAs[category][Question #][0 - id / 1 - q / 2 - a]"""
    print("Categories:", QAs.keys())
    print("Questions and Answers:\n", QAs)
    for cat, qs in QAs.items():
        print(cat + ":")
        for q in qs:
            print(q[0], q[1], "\n\t", q[2])

