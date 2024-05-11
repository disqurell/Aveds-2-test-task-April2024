from db.base import DbController


class Utils:
    controller = DbController

    def get_tg_bot_token(self, uuid):
        user = self.find_user_by_field("uuid", uuid)

        return user[0][-1]

    def find_user_by_field(self, field_name: str, field_value: str):
        user = self.controller.select_from_table_with_condition(
            "users", field_name, field_value
        )

        return user
