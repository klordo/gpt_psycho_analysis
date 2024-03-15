import json

from questions import questions, final_questions
from gpt import debug_subject_ask, debug_subject_sum, debug_final_ask
from gpt import subject_ask_gpt_3_5, subject_sum_gpt_4, finally_ask_gpt_4


with open('user_text.txt', 'r', encoding='utf8') as f:
    user_input = '\n'.join(f.readlines())


def save_all_answers(debug=True, stride=3, final_stride=5):
    answers_json = {
        'user_input': user_input,
        'answers': {},
        'subject_sum': {},
        'final_answers': {}
    }

    # Каждая тема по stride вопросов
    for subject, q_list in questions.items():
        print(f"{subject}")

        answers_json['answers'][subject] = []

        for i in range(0, len(q_list), stride):
            part_questions = q_list[i:i + stride]

            if debug:
                result = debug_subject_ask(subject, part_questions, user_input)
            else:
                result = subject_ask_gpt_3_5(subject, part_questions, user_input)

            answers_json['answers'][subject].append(result)

            with open('answers.json', 'w', encoding='utf8') as file:
                json.dump(answers_json, file, indent=4, ensure_ascii=False)

    # Вывод тем
    # тут соединяю ответы из списка словарей в один абзац
    for subject, question_list in answers_json['answers'].items():
        subject_answers = []
        for item in question_list:
            subject_answers.append(f"{item['questions']} {item['answer']}")
        subject_answers = '\n'.join(subject_answers)

        if debug:
            result = debug_subject_sum(subject, subject_answers)
        else:
            result = subject_sum_gpt_4(subject, subject_answers)

        answers_json['subject_sum'][subject] = result

        with open('answers.json', 'w', encoding='utf8') as file:
            json.dump(answers_json, file, indent=4, ensure_ascii=False)

    full_subject_sum = [answers_json['subject_sum'][subject]['answer'] for subject in questions.keys()]
    full_subject_sum = '\n'.join(full_subject_sum)
    answers_json['subject_sum']['full_subject_sum'] = full_subject_sum

    # Финальные вопросы
    for subject, q_list in final_questions.items():
        print(f"{subject}")

        answers_json['final_answers'][subject] = []

        for i in range(0, len(q_list), final_stride):
            part_questions = q_list[i:i + final_stride]

            if debug:
                result = debug_final_ask(subject, part_questions, full_subject_sum)
            else:
                result = finally_ask_gpt_4(subject, part_questions, full_subject_sum)

            answers_json['final_answers'][subject].append(result)

            with open('answers.json', 'w', encoding='utf8') as file:
                json.dump(answers_json, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # test_gpt_is_working()
    save_all_answers(debug=True)