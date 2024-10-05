from abc import abstractmethod
import time


class User:
    def __init__(self):
        self.permission = ''

    @abstractmethod
    def get_permissions(self):
        pass


class AdminUser(User):
    def get_permissions(self):
        print('Получены права Админа')
        self.permission = 'Admin'

    def check_permission(self):
        print(self.permission)


class ManagerUser(User):
    def get_permissions(self):
        print('Получены права Менеджера')
        self.permission = 'Manager'

    def check_permission(self):
        print(self.permission)


class GuestUser(User):
    def get_permissions(self):
        print('Получены права Гостя')
        self.permission = 'Guest'

    def check_permission(self):
        print(self.permission)


class UserFactory:
    @staticmethod
    def create_user(user_type):
        if user_type == 'Admin':
            return AdminUser()
        elif user_type == 'Manager':
            return ManagerUser()
        elif user_type == 'Guest':
            return GuestUser()


def main():
    factory = UserFactory()
    print('Добро пожаловать в систему создания пользователей!\nМеню:')
    print('1. Админ\n2. Менеджер\n3. Гость\n0. Назад')
    create = int(input('Выберете пользователя:'))
    if create == 1:
        admin = factory.create_user('Admin')
        print(f'Создан пользователь Админ')
        admin.get_permissions()
        print('Проверка прав доступа...')
        time.sleep(2)
        print(f'У этого пользователя права типа:')
        admin.check_permission()
    elif create == 2:
        manager = factory.create_user('Manager')
        print(f'Создан пользователь Менеджер')
        manager.get_permissions()
        print('Проверка прав доступа...')
        time.sleep(2)
        print(f'У этого пользователя права типа:')
        manager.check_permission()
    elif create == 3:
        guest = factory.create_user('Guest')
        print(f'Создан пользователь Гость')
        guest.get_permissions()
        print('Проверка прав доступа...')
        time.sleep(2)
        print(f'У этого пользователя права типа:')
        guest.check_permission()


if __name__ == '__main__':
    main()
