class MailMerge:
    def __init__(self, letter_fn, user_list_fn, output_folder):
        self.letter_fn = letter_fn
        self.user_list_fn = user_list_fn
        self.output_folder = output_folder
        self.letter_contents = []
        self.user_list = []

    def read_input_files(self):
        with open(self.letter_fn) as file:
            self.letter_contents = file.readlines()
        with open(self.user_list_fn) as file:
            self.user_list = file.readlines()

    def perform_mail_merge(self):

        for user in self.user_list:
            user_name = user.strip('\n')
            output_file_name = f"{self.output_folder}letter_for_{user_name}.txt"
            greeting_line = self.letter_contents[0].replace('[name]', user_name)

            with open(output_file_name, 'w') as file:
                file.write(greeting_line)
                file.writelines(self.letter_contents[1:])


mm = MailMerge('./Input/Letters/starting_letter.txt', './Input/Names/invited_names.txt', './Output/ReadyToSend/')
mm.read_input_files()
mm.perform_mail_merge()
