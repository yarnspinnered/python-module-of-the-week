import textwrap

sample_paragraph = """  
    Python is an interpreted high-level programming language for general-purpose programming.
    Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. 
    It provides constructs that enable clear programming on both small and large scales.[27] 
    In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.[28][29]

    Python features a dynamic type system and automatic memory management. 
    It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[30] 
"""

wrapped = textwrap.fill(sample_paragraph, 70)
dedented = textwrap.dedent(sample_paragraph)
dedented_then_wrapped = textwrap.fill(dedented,60)
print("Wrapped version")
print(wrapped)
print("Dendeted version")
print(dedented)
print("Dedented then wrapped version")
print(dedented_then_wrapped)
print(dedented_then_wrapped[0])

print("Indented with a >")
print(textwrap.indent(dedented_then_wrapped, "> "))

