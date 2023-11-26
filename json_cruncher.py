import orjson,os,pprint

def butfy(alldata):
    return orjson.dumps(alldata,option=orjson.OPT_INDENT_2).dencode('UTF-8')

def write_jfile(filename,filedata):
    if os.path.splitext(filename)[1][1:] != "json":
        filename = os.path.splitext(filename)[0]+".json"
    if os.path.exsist(os.path.join(os.getcwd(),filename)) and os.path.isfile(filename):
        if input("overwrite y/n:").lower() in ["y","yes"]:
            with open(filename,"w") as jfile:
                jfile.write(butfy(filedata))
        else:
            filename=input("enter the new filename:")
            if file.isEmpty():
                filename = defaultname
            with open(filename,"w") as jfile:
                jfile.write(butfy(filedata))

def exit_or_not(dispmessage):
    if input(f"exit the {dispmessage} block:").lower() in ["y","yes","yep"]:
        return False
    else:
        return True

def isit(yesorno):
    if yesorno.lower() in ["yes","yep","y"]:
        return False
    else:
        return True
def find_word(context,sentence):
    return int(intput("Enter the index:"))
    

def run_block():
    data=[]
    while exit_or_not("context block"):
        qas = []
        context_input = {"context":"","qas":[]}
        context = input("Enter the apt context:")
        context_input["context"] = context
        while exit_or_not("question block"):
            answers = []
            qas_input = {"id":"","is_impossible":"","question":"","answers":[]}
            id_input = input("Enter the question id:")
            is_impossible_input = input("Is it possible:")
            question_input = input("Enter the apt question:")
            qas_input["id"] = id_input
            qas_input["is_impossible"] = isit(is_impossible_input)
            qas_input["question"] = question_input
            while exit_or_not("answer block"):
                answers_input={"text":"","answer_start":0}
                text_input = input("Enter the apt answer:")
                answers_input["text"] = text_input
                answers_input["answer_start"] = find_word(context,text_input) #  needs some work here
                answers.append(answers_input)
                dmes(answers)
            qas_input["answers"] = answers
            qas.append(qas_input)
        context_input["qas"] = qas
        data.append(context_input)
    return data
