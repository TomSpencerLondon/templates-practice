from flask import Flask, Blueprint, render_template, request

main = Blueprint('main', __name__)


@main.route('/nodes')
def nodes():
    return render_template('nodes.html')

@main.route('/template')
def template():
    return render_template('template.html')

@main.route('/add')
def add():
    return render_template('add-question.html')

@main.route('/api/formadd', methods=['POST'])
def add_post_form():
    print(request.form)
    return 'submitted'

@main.route('/api/jsonadd', methods=['POST'])
def add_post_json():
    print(request.get_json())
    return 'submitted'

@main.route('/api')
def index():
    return {'data' : 
    [
        {
            "text": "## SingleChoice\r\n\r\n```\r\nclass SingleChoice {\r\n  private final String singleChoice;\r\n}\r\n```",
            "answer": "Choice 1",
            "choices": [
                "Choice 1",
                "Choice 2",
                "Choice 3",
                "Choice 4"
            ]
        },
        {
            "text": "### MultipleChoice\r\n\r\n```\r\nclass MultipleChoice {\r\n  private final List<String> multipleChoice;\r\n}\r\n```",
            "answer": "Multiple Choice 1, Multiple Choice 2",
            "choices": [
                "Multiple Choice 1",
                "Multiple Choice 2",
                "Multiple Choice 3",
                "Multiple Choice 4"
            ]
        },
        {
            "text": "Q1",
            "answer": "A5",
            "choices": [
                "A1",
                "A2",
                "A3",
                "A4",
                "A5"
            ]
        },
        {
            "text": "Question Single",
            "answer": "Choice 2",
            "choices": [
                "Choice 1",
                "Choice 2",
                "Choice 3",
                "Choice 4"
            ]
        },
        {
            "text": "Another single question",
            "answer": "Choice 1",
            "choices": [
                "Choice 1",
                "Choice 2",
                "Choice 3",
                "Choice 4"
            ]
        },
        {
            "text": "Single choice question",
            "answer": "SC1",
            "choices": [
                "SC1",
                "SC2",
                "SC3",
                "SC4"
            ]
        },
        {
            "text": "Single Choice",
            "answer": "SC4",
            "choices": [
                "SC1",
                "SC2",
                "SC3",
                "SC4"
            ]
        },
        {
            "text": "Single choice question again",
            "answer": "S1",
            "choices": [
                "S1",
                "S2",
                "S3",
                "S4",
                "S5",
                "S6"
            ]
        },
        {
            "text": "### New question\r\n\r\n```\r\nclass Question {\r\n  private String answer;\r\n}\r\n```",
            "answer": "Answer 2",
            "choices": [
                "Answer 1",
                "Answer 2",
                "Answer 3",
                "Answer 4",
                "Answer 5"
            ]
        },
        {
            "text": "new Question",
            "answer": "Answer 5",
            "choices": [
                "Answer 1",
                "Answer 2",
                "Answer 3",
                "Answer 4",
                "Answer 5"
            ]
        },
        {
            "text": "#### I am \r\n```\r\nclass Learn {\r\n  String java;\r\n}\r\n```",
            "answer": "answer 1",
            "choices": [
                "answer 1",
                "Answer 2",
                "answer 3"
            ]
        },
        {
            "text": "# New question\r\n\r\n```\r\nclass NewQuestion {\r\n  String question;\r\n}\r\n```",
            "answer": "answer 1",
            "choices": [
                "answer 1",
                "answer 2",
                "answer 3"
            ]
        },
        {
            "text": "# Single Choice\r\n\r\nclass Question {\r\n  String java;\r\n}",
            "answer": "answer 1",
            "choices": [
                "answer 1",
                "answer 2",
                "answer 3",
                "answer 4"
            ]
        },
        {
            "text": "# Hello\r\n\r\n```\r\nclass Hello {\r\n  String java;\r\n}\r\n```",
            "answer": "Answer 1",
            "choices": [
                "Answer 1",
                "Answer 2",
                "Answer 3",
                "Answer 4"
            ]
        },
        {
            "text": "# next question\r\n```\r\nclass Question {\r\n  String question;\r\n}\r\n```",
            "answer": "1 answer",
            "choices": [
                "1 answer",
                "2 answer",
                "3 answer",
                "4 answer"
            ]
        },
        {
            "text": "# Question 1\r\n\r\nclass Question {\r\n  Integer one = 1;\r\n}",
            "answer": "Correct 1",
            "choices": [
                "Correct 1",
                "Incorrect 2"
            ]
        }
    ]}

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    return app

if __name__ == "__main__":  # There is an error on this line
    create_app().run()
