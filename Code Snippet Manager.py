class CodeSnippetManager:
    def __init__(self):
        self.snippets = {}

    def add_snippet(self, name, code):
        self.snippets[name] = code

    def get_snippet(self, name):
        return self.snippets.get(name, "Snippet not found")

# Example usage:
manager = CodeSnippetManager()
manager.add_snippet("Hello World", "print('Hello, world!')")
print(manager.get_snippet("Hello World"))
