import ast


def build_syntax_tree(program_text):
    try:
        syntax_tree = ast.parse(program_text)
    except SyntaxError:
        syntax_tree = None
    return syntax_tree


def extract_func_names(program_text):
    syntax_tree = build_syntax_tree(program_text)
    if not syntax_tree:
        return []
    func_names = [node.name.lower() for node in ast.walk(syntax_tree) if isinstance(node, ast.FunctionDef)]
    return func_names


def split_name_to_words(name):
    return [word for word in name.split('_') if word]
