from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY)


def test_gpt_is_working():
    print('Wait answer from GPT...')
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': "Say 'Hello world!'"}],
    )
    answer = response.choices[0].message.content.strip()
    print(answer)


def debug_subject_ask(subject, part_questions, user_input):
    short_prompt = \
        f'Ты суперпсихолог по теме {subject}\n' \
        f'Ответь на вопросы: {"; ".join(part_questions)}\n'

    full_prompt = short_prompt + "Текст эссе: " + user_input

    tokens = {"completion_token": 7, "prompt_tokens": 3, "total_tokens": 10}

    result = {
        'questions': "; ".join(part_questions),
        'prompt': short_prompt,
        'answer': "Ответ ChatGPT на промпт",
        'tokens': tokens
    }
    return result


def debug_subject_sum(subject, subject_answers):
    prompt = \
        f"Сделай наиболее полный вывод по теме {subject}:\n" \
        f"{subject_answers}"

    tokens = {"completion_token": 7, "prompt_tokens": 3, "total_tokens": 10}

    result = {
        'prompt': prompt,
        'answer': "Ответ ChatGPT на промпт вывода темы",
        'tokens': tokens
    }
    return result


def debug_final_ask(subject, part_questions, full_subject_sum):
    short_prompt = \
        f'Ты суперпсихолог по теме {subject}\n' \
        f'Ответь на вопросы: {"; ".join(part_questions)}\n'

    full_prompt = short_prompt + f'Используя выводы ниже: ' + full_subject_sum

    tokens = {"completion_token": 7, "prompt_tokens": 3, "total_tokens": 10}

    result = {
        'questions': "; ".join(part_questions),
        'prompt': short_prompt,
        'answer': "Финальный ответ ChatGPT на промпт",
        'tokens': tokens
    }
    return result


def subject_ask_gpt_3_5(subject, part_questions, user_input):
    system_content = f'You are a professional psycholinguist in the field of "{subject}" performing text analysis. ' \
                     f'Your task is to draw conclusions based on the patients text.'

    content = f"Questions: {'; '.join(part_questions)}. Analyze the essay below using the previous question: {user_input}"

    messages = [
        {'role': 'system', 'content': system_content},
        {'role': 'user', 'content': content},
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )
    message = response.choices[0].message.content.strip()
    tokens = {
        "completion_token": response.usage.completion_tokens,
        "prompt_tokens": response.usage.prompt_tokens,
        "total_tokens": response.usage.total_tokens
    }

    return message, tokens


def subject_sum_gpt_4(subject, subject_answers):
    system_content = f'You are a professional psycholinguist in the field of "{subject}" summarize text.'
    content = f"{subject_answers}"

    messages = [
        {'role': 'system', 'content': system_content},
        {'role': 'user', 'content': content},
    ]

    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=messages,
        temperature=0.3,
        max_tokens=4096,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )
    message = response.choices[0].message.content.strip()
    tokens = {
        "completion_token": response.usage.completion_tokens,
        "prompt_tokens": response.usage.prompt_tokens,
        "total_tokens": response.usage.total_tokens
    }

    return message, tokens


def finally_ask_gpt_4(subject, part_questions, full_subject_sum):
    system_content = f'Ты суперпсихолог по теме {subject}\n'

    content = f"Questions: {'; '.join(part_questions)}. Используя выводы ниже: {full_subject_sum}"

    messages = [
        {'role': 'system', 'content': system_content},
        {'role': 'user', 'content': content},
    ]

    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=messages,
        temperature=0.3,
        max_tokens=4096,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )
    message = response.choices[0].message.content.strip()
    tokens = {
        "completion_token": response.usage.completion_tokens,
        "prompt_tokens": response.usage.prompt_tokens,
        "total_tokens": response.usage.total_tokens
    }

    return message, tokens
