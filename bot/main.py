import telebot
from telebot import types

bot = telebot.TeleBot('6248207182:AAE6lJ6mMoZeotAQVfH96J982tcIuUZvCnw')

questions = [
    {
        'text': '1. Розвяжіть нерівність: x^2 + 2x - 8 > 0',
        'options': [
            '(-4; 2)',
            '(-∞; -4) ∪ (2; +∞)',
            '(-∞; -4] ∪ [2; +∞)',
            '∅'
        ],
        'correct': 1
    },
    {
        'text': '2. Розвяжіть нерівність: x^2 - 4x + 3 < 0',
        'options': [
            '(0; 3)',
            '(-∞; 1) ∪ (3; +∞)',
            '(1; 3)',
            '(-∞; 0) ∪ (3; +∞)'
        ],
        'correct': 2
    },
    {
        'text': '3. Розвяжіть нерівність: 3x^2 - 6x - 15 < 0',
        'options': [
            '(-∞; -1) ∪ (5; +∞)',
            '(-∞; -1] ∪ [5; +∞)',
            '(-1; 5)',
            '∅'
        ],
        'correct': 2
    },
    {
        'text': '4. Розвяжіть нерівність: 2x^2 - 8x + 6 < 0',
        'options': [
            '(1; 3)',
            '(-∞; 1) ∪ (3; +∞)',
            '(-1; 2)',
            '∅'
    ],
        'correct': 1
    },
    {
        'text': '5. Розвяжіть нерівністьо: 4x^2 - 12x + 9 < 0',
        'options': [
            '(-∞; 1) ∪ (3; +∞)',
            '(1; 3)',
            '(1; 3]',
            '∅'
    ],
        'correct': 4
    },
    {
        'text': '6. Розвяжіть нерівність: x^2 - 8x + 16 ≥ 0',
        'options': [
            '(4; +∞)',
            '(-∞; 4) ∪ (4; +∞)',
            '(-∞; 4]',
            '[4; +∞)'
    ],
        'correct': 4
    },
    {
        'text': '7. Розвяжіть нерівність: x^2 + 6x + 8 > 0',
        'options': [
            '(-∞; -4) ∪ (-2; +∞)',
            '(-∞; -4] ∪ (-2; +∞)',
            '(-2; 2)',
            '(-∞; -2] ∪ [2; +∞)'
    ],
        'correct': 2
    },
    {
        'text': '8. Розвяжіть нерівність: -3x^2 - 12x - 9 > 0',
        'options': [
            '(-∞; -3) ∪ (1; +∞)',
            '(1; +∞)',
            '(-1; 0)',
            '∅'
    ],
        'correct': 1
    },
    {
        'text': '9. Розвяжіть нерівність: 2x^2 + 4x - 6 ≤ 0',
        'options': [
            '(-∞; -3] ∪ [1; +∞)',
            '(-3; 1)',
            '(-∞; -3) ∪ (1; +∞)',
            '∅'
    ],
        'correct': 1
    },
    {
        'text': '10. Решите неравенство: 6x^2 - 24x + 18 ≥ 0',
        'options': [
            '(1; 3)',
            '(-∞; 1) ∪ (3; +∞)',
            '(1; 3]',
            '∅'
    ],
        'correct': 2
    }
]

answers = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Пройдіть тест по алгебрі за темою квадратичні нерівності')
    ask_question(message.chat.id, 0)

def ask_question(chat_id, question_index):
    if question_index == len(questions):
        score = sum(answers.values())
        bot.send_message(chat_id, f'Тест завершено, ваш бал: {score}')
    else:
        question = questions[question_index]
        text = question['text']
        options = question['options']

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for option in options:
            markup.add(types.KeyboardButton(option))

        bot.send_message(chat_id, text, reply_markup=markup)
        bot.register_next_step_handler_by_chat_id(chat_id, check_answer, question_index)

def check_answer(message, question_index):
    question = questions[question_index]
    correct_answer = question['correct']
    user_answer = question['options'].index(message.text) + 1
    answers[question_index] = int(correct_answer == user_answer)
    ask_question(message.chat.id, question_index + 1)

bot.polling()
