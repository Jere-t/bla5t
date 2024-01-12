class Ability:
    def __init__(
        self,
        value: int,
        sub_value: int = 0,
        text_en: str = None,
        text_fr: str = None,
        ability_icon=None,
    ):
        self.value = value
        self.sub_value = sub_value
        self.text_en = text_en
        self.text_fr = text_fr
        self.ability_icon = ability_icon

    def switch_case_exemple(case_value: float):
        if case_value == 0.1:
            print("handle_case_zero(1)")
        elif case_value == 0.2:
            print("handle_case_zero(2)")
        elif case_value == 0.3:
            print("handle_case_zero(3)")
        elif case_value == 0.4:
            print("handle_case_zero(4)")
        elif case_value == 1.0:
            print("handle_case_one(4)")
        elif case_value == 2.0:
            print("handle_case_two(4)")
        elif case_value == 3.0:
            print("handle_case_three(4)")
        # ...
        else:
            print("Default case")
