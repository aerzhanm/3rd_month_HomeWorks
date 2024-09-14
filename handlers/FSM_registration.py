from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM_reg(StatesGroup):
    fullname = State()
    date_of_birth = State()
    phon_num = State()
    email_1 = State()
    photo_1 = State()


async def start_fsm_reg(m: types.Message):
    await m.answer('Введите ФИО:')
    await FSM_reg.fullname.set()


async def load_fullname(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = m.text

    await m.answer('Введите дату рождения (в формате ДД.ММ.ГГГГ):')
    await FSM_reg.date_of_birth.set()


async def load_date(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date_of_birth'] = m.text

    await m.answer('введите номер телефона:')
    await FSM_reg.phon_num.set()


async def load_phon_num(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phon_num'] = m.text

    await m.answer('введите ваш email adress:')
    await FSM_reg.email_1.set()


async def load_email(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email_1'] = m.text

    await m.answer('отправьте фото:')
    await FSM_reg.photo_1.set()


async def load_photo(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo_1'] = m.photo[-1].file_id

    await m.answer_photo(
         photo=data['photo_1'],
         caption=f'Верные ли ответы?\n\n'
                 f'ФИО: {data["fullname"]}\n'
                 f'Дата рождения: {data["date_of_birth"]}\n'
                 f'номер телефона: {data["phon_num"]}\n'
                 f'email adress {data["email_1"]}'
    )
    await state.finish()  # Завершаем состояние




def register_fsm(dp: Dispatcher):
    dp.register_message_handler(start_fsm_reg, commands=['reg'], state='*')
    dp.register_message_handler(load_fullname, state=FSM_reg.fullname)
    dp.register_message_handler(load_date, state=FSM_reg.date_of_birth)
    dp.register_message_handler(load_phon_num, state=FSM_reg.phon_num)
    dp.register_message_handler(load_email, state=FSM_reg.email_1)
    dp.register_message_handler(load_photo, state=FSM_reg.photo_1,
                                content_types=['photo'])
