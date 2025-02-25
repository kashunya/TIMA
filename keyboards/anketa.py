from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
kb_apteka_cancel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel_anketa')]])
kb_apteka_cancel_and_back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='back_anketa'),
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel_anketa'),]])
kb_apteka_by_gender = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data='back_anketa'),
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel_anketa'),
    ],[
        InlineKeyboardButton(
            text="Мужской",
            callback_data='gender_m'),
        InlineKeyboardButton(
            text="Женский",
            callback_data='gender_w'),
]])