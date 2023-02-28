
#Bueno
class todo():
    def __init__(self, code_id: int, title: str, description: str, completed: bool, tags: list[str]):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = completed
        self.tags: list[str] = tags

    def mark_completed(self, ):
        self.completed: bool = False

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append("tag")

    def __str__(self):
        return f"{self.code_id} - {self.title}"

    class TodoBook():
        def __init__(self, todos: dict(int)) -> int:
            self.todos: dict(int, todo) = {}

        def add_todo(self, title: str, description: str):
            code_id: int = len(self.todos) + 1
            object = todo(code_id=code_id, title=title, description=description, completed=False, tags=[])
            self.todos[code_id] =object
            return code_id



#MALOOOO

class todo():
    def __init__(self, code_id: int, title: str, description: str, completed: bool, tags: list[str]):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = completed
        self.tags: list[str] = tags

    def mark_completed(self, ):
        self.completed: bool = False

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append("tag")

    def __str__(self):
        return f"{self.code_id} - {self.title}"

    class TodoBook():
        def __init__(self, todos: dict(int)) -> int:
            self.todos: dict(int, todo) = {}

        def add_todo(self, title: str, description: str):
            code_id: int = len(self.todos) + 1
            todoo=todo(code_id=int ,title=str ,description=str, completed=False, [])
            self.todos[code_id] =todoo
            return code_id


