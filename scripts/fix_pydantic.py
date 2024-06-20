""" Using ast transformer to fix issues with automatic pydantic generation"""

import ast
import sys

import astor


class ClassRemover(ast.NodeTransformer):
    def __init__(self, class_name):
        self.class_name = class_name

    def visit_ClassDef(self, node):
        # Remove the class if its name matches the class_to_remove
        if node.name == self.class_name:
            return None
        return node

    def visit_Expr(self, node):
        # Check if the node is a call expression
        if isinstance(node.value, ast.Call):
            # Check if the call expression is an attribute (method call)
            if isinstance(node.value.func, ast.Attribute):
                # Check if the method call matches the specified class
                if (
                    isinstance(node.value.func.value, ast.Name)
                    and node.value.func.value.id == self.class_name
                ):
                    return None  # Remove this node
        return self.generic_visit(node)


class TypeReplacer(ast.NodeTransformer):
    def __init__(self, old_type, new_type):
        self.old_type = old_type
        self.new_type = new_type

    def visit_FunctionDef(self, node):
        # Check all arguments in the function definition
        for arg in node.args.args:
            if arg.annotation:
                arg.annotation = self.visit(arg.annotation)
        return self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        # Handle async function definitions similarly
        for arg in node.args.args:
            if arg.annotation:
                arg.annotation = self.visit(arg.annotation)
        return self.generic_visit(node)

    def visit_Name(self, node):
        # Replace the old type with the new type
        if node.id == self.old_type:
            node.id = self.new_type
        return node

    def visit_Subscript(self, node):
        # Handle Union, Optional, and other subscripted types
        node.value = self.visit(node.value)
        node.slice = self.visit(node.slice)
        return node

    def visit_Index(self, node):
        # Handle the index part of subscripted types
        node.value = self.visit(node.value)
        return node

    def visit_Tuple(self, node):
        # Handle tuples in type annotations
        node.elts = [self.visit(elt) for elt in node.elts]
        return node


def edit_pydantic(input_file, output_file):

    with open(input_file, "r") as file:
        tree = ast.parse(file.read())

    transformer_class = ClassRemover(class_name="LangString")
    tree_modclass = transformer_class.visit(tree)

    transformer_tp = TypeReplacer(
        old_type="LangString", new_type="Dict[str, str]"
    )
    tree_modclass_modtype = transformer_tp.visit(tree_modclass)

    with open(output_file, "w") as file:
        file.write(astor.to_source(tree_modclass_modtype))


if __name__ == "__main__":
    input_file = sys.argv[1]
    if len(sys.argv) < 3:
        output_file = input_file
    else:
        output_file = sys.argv[2]
    print(
        f"Fixing automatically generated pydantic file {input_file} "
        f"and saving to {output_file}"
    )
    edit_pydantic(input_file, output_file)
