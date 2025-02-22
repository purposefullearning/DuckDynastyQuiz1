from flask import Flask, request, render_template_string

app = Flask(__name__)

quiz = [
    {"question": "What is the name of the family business featured in Duck Dynasty?", "options": ["A. Duck Commander", "B. Duck Hunters Inc.", "C. Beard Bros", "D. Cajun Calls"], "answer": "A"},
    {"question": "Which Robertson family member is known for his wild stories and iced tea obsession?", "options": ["A. Phil", "B. Willie", "C. Si", "D. Jase"], "answer": "C"},
    {"question": "In what state does the Robertson family live?", "options": ["A. Texas", "B. Louisiana", "C. Alabama", "D. Mississippi"], "answer": "B"},
    {"question": "What ZZ Top song is used as the theme for Duck Dynasty?", "options": ["A. La Grange", "B. Sharp Dressed Man", "C. Gimme All Your Lovin'", "D. Legs"], "answer": "B"},
    {"question": "What did Phil Robertson invent that started the Duck Commander empire?", "options": ["A. Camouflage Pants", "B. Duck Call", "C. Beard Trimmer", "D. Fishing Lure"], "answer": "B"},
    {"question": "Which brother is the CEO of Duck Commander?", "options": ["A. Jase", "B. Jep", "C. Willie", "D. Alan"], "answer": "C"},
    {"question": "What does Uncle Si call almost everyone he meets?", "options": ["A. Buddy", "B. Jack", "C. Partner", "D. Hoss"], "answer": "B"},
    {"question": "What sport did Phil Robertson play in college before turning down an NFL career?", "options": ["A. Baseball", "B. Football", "C. Basketball", "D. Wrestling"], "answer": "B"},
    {"question": "What unusual item did Si win in a raffle at the donut shop?", "options": ["A. A Lawnmower", "B. A Camper", "C. A Duck Boat", "D. A Giant Duck Call"], "answer": "B"},
    {"question": "Which family member released a cookbook called 'Miss Kay’s Duck Commander Kitchen'?", "options": ["A. Korie", "B. Missy", "C. Kay", "D. Sadie"], "answer": "C"},
    {"question": "What did Willie accidentally hit Korie with while training for a family football game?", "options": ["A. A Football", "B. A Duck Call", "C. A Lawn Chair", "D. A Fishing Rod"], "answer": "A"},
    {"question": "What did the Duck Commander employees build to celebrate the company’s 40th anniversary?", "options": ["A. World’s Largest Duck Call", "B. A Giant Beard Statue", "C. A Duck Blind", "D. A Camo Truck"], "answer": "A"},
    {"question": "Which country did Willie take the family to after landing a client for duck calls?", "options": ["A. Canada", "B. Scotland", "C. Australia", "D. Ireland"], "answer": "B"},
    {"question": "What does the show typically end with the family doing?", "options": ["A. Hunting Ducks", "B. Praying Around the Table", "C. Singing a Song", "D. Telling Jokes"], "answer": "B"}
]

@app.route('/', methods=['GET', 'POST'])
def quiz_page():
    if request.method == 'POST':
        score = 0
        for i, q in enumerate(quiz):
            if request.form.get(f'q{i}') == q['answer']:
                score += 1
        percentage = (score / len(quiz)) * 100
        result = f"Score: {score}/{len(quiz)} ({percentage}%) - Share with #DuckDynastyQuiz on X!"
        return render_template_string('<h1>{{result}}</h1><a href="/">Play Again</a>', result=result)
    
    html = '<h1>Duck Dynasty Quiz</h1><form method="post">'
    for i, q in enumerate(quiz):
        html += f'<p>{q["question"]}</p>'
        for opt in q["options"]:
            html += f'<input type="radio" name="q{i}" value="{opt[0]}" required> {opt}<br>'
    html += '<br><input type="submit" value="Submit"></form>'
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)