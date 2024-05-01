class Human_parameters:
    def __init__(self, name, age, gender, search_of):
        self.name = name
        self.age = age
        self.gender = gender
        self.search_of = search_of

    def get_parameters(self):
        return [self.name, self.age, self.gender, self.search_of]


class Human_music:
    def __init__(self, music_list):
        self.music_list = music_list

    def get_parameters(self):
        return [self.music_list]


class Human_Description:
    def __init__(self, description):
        self.description = description

    def get_parameters(self):
        return [self.description]


class Human_images:
    def __init__(self, images: list):
        self.images = images

    def get_parameters(self):
        return [self.images]


class Form:
    def __init__(self, name: str, age: int, gender: str, search_of: str, music: str, description: str, images: list):
        self.parameters = Human_parameters(name, age, gender, search_of)
        self.music = Human_music(music)
        self.description = Human_Description(description)
        self.images = Human_images(images)

    def get_parameters(self):
        return [self.parameters.get_parameters(), self.music.get_parameters(), self.description.get_parameters(),
                self.images.get_parameters()]
