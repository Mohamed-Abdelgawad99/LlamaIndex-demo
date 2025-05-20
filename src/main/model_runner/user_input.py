class UserInput:
    def __init__(self, system_instruction_options):
        self.system_instruction_options = system_instruction_options

    def display_options(self):
        print(
            "Please Enter FrameWork Type you are wokring on"
            "by selecting form the following: \n"
        )
        for i, option in enumerate(self.system_instruction_options, 1):
            print(f"{i}. {option}")

    def get_user_choice(self):
        while True:
            try:
                choice = int(input())
                if choice <= len(self.system_instruction_options) and choice > 0:
                    return self.system_instruction_options[choice - 1]
                else:
                    print("Invalid choice. Please choose again. ")
                    self.display_options()
            except:  # noqa: E722
                print("Invalid choice. Please choose again.")
                self.display_options()
