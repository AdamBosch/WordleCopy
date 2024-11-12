from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)
with open("valid-wordle-words.txt", 'r') as file:
    lines = file.readlines()

wordle_word = "Flask"

@app.route('/')
def main():
    return render_template("main.html")

@app.route("/api/check_input", methods=["POST"])
def check_word():
    result_dict = [[] for _ in range(len(wordle_word))]
    content = request.get_json()
    test_word = content.get("word")
    print(test_word)
    if (test_word.lower() + "\n") not in lines:
        print("not a word")
        return "Incorrect word", 300
    test_word_lst = list(test_word)
    wordle_word_lst = list(wordle_word)

    for i in range(len(wordle_word_lst)):
        if test_word_lst[i] == wordle_word_lst[i]:
            result_dict[i] = [wordle_word_lst[i], "green"]
        elif test_word_lst[i] in wordle_word_lst:
            result_dict[i] = [test_word_lst[i], "yellow"]
        else:
            result_dict[i] = [test_word_lst[i], "red"]

    return jsonify(result_dict=result_dict)

@app.route("/api/choose_word", methods=['POST'])
def choose_word():
    global wordle_word
    index = random.randrange(0, (len(lines)-1))
    wordle_word = lines[index].strip().upper()
    print("new word: " + wordle_word)
    return "Success", 200
        
if __name__ == "__main__":
    app.run(debug=True)