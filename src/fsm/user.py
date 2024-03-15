from aiogram.fsm.state import State, StatesGroup


class TextAnalys(StatesGroup):
    wait_text = State()