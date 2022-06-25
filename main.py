from utils import Utils


def main():
    print('Приветик! Данная программа обслуживает логистику'
          '\nДля начала работы нажмите Enter\n'
          'Для остановки программы введите "стоп"\n'
          '\nДля взаимодействия с программой необходимо ввести команды:\n'
          '\nФормат: Доставить [кол-во] [наименование] из [откуда] в [куда]\n'
          'Пример: Доставить 1 пивко из склад в магазин')
    input()

    shop, store = Utils.create_instances()

    while True:
        print(Utils.display_items(store=store, shop=shop))
        user_task = input('\nВведите задание: ')
        print(Utils.send_request(user_task, shop, store))


if __name__ == '__main__':
    main()
