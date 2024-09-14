from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from buttons import sizes, cen_button, submit_button


class FSM_store(StatesGroup):
    name = State()
    size = State()
    category = State()
    price = State()
    product_id = State()
    photo = State()
    submit = State()


size = ['XL', 'XXL', '3XL', 'M', 'L']


async def fsm_store(m: types.Message):
    await m.answer('Название тавара:')
    await FSM_store.name.set()


async def load_name_1(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = m.text

    await m.answer('Укажите размер тавара:', reply_markup=sizes)
    await FSM_store.size.set()


async def load_size(m: types.Message, state: FSMContext):
    if m.text in size:
        async with state.proxy() as data:
            data['size'] = m.text

        await m.answer('Укажите котегорию  тавара:')
        await FSM_store.category.set()
    else:
        await m.answer('нажмите на кнопки!!')


async def load_category(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = m.text

    await m.answer('Укажите цену тавара:')
    await FSM_store.price.set()


async def load_price(m: types.Message, state: FSMContext):
    if m.text.isdigit():
        async with state.proxy() as data:
            data['price'] = m.text
        await m.answer('Отправьте фото:')
        await FSM_store.photo.set()

    else:
        await m.answer('введите цену цифрами!!')


async def load_photo(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = m.photo[-1].file_id

    await m.answer('Введите id тавара:')
    await FSM_store.product_id.set()


async def product_id(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = m.text


    await m.answer_photo(photo=data['photo'],
                         caption=f'Название: {data["name"]}\n'
                                 f'Размер: {data["size"]}\n'
                                 f'Категория: {data["category"]}\n'
                                 f'Цена: {data["price"]}\n'
                                 f'Верные ли данные?',
                         reply_markup=submit_button)

    await FSM_store.next()


async def submit(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()

    if message.text == 'Да':
        await message.answer('Отлично, Данные в базе!', reply_markup=kb)
        await state.finish()

    elif message.text == 'Нет':
        await message.answer('Хорошо, заполнение анкеты завершено!', reply_markup=kb)
        await state.finish()

    else:
        await message.answer('Выберите "Да" или "Нет"')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    kb = ReplyKeyboardRemove()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=cen_button)


def register_store(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена', ignore_case=True), state="*")
    dp.register_message_handler(fsm_store, commands=['store'])
    dp.register_message_handler(load_name_1, state=FSM_store.name)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_photo, state=FSM_store.photo,
                                content_types=['photo'])
    dp.register_message_handler(product_id, state=FSM_store.product_id)
    dp.register_message_handler(submit, state=FSM_store.submit)
