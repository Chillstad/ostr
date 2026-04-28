from commands.command import Command

def test_arg_parse_a() -> None:
    c : Command = Command()
    parsed_args = c.parse_args("--debug Hello, World!")
    assert(parsed_args == {"debug": "Hello, World!"})

def test_arg_parse_b() -> None:
    c : Command = Command()
    parsed_args = c.parse_args("--debug Hello, World! --invalid This is a test")
    assert(parsed_args == {"debug": "Hello, World!"})

def test_arg_parse_c() -> None:
    c : Command = Command()
    parsed_args = c.parse_args("--debug --debug --debug")
    assert(parsed_args == {"debug": ""})

def test_arg_parse_d() -> None:
    c : Command = Command()
    parsed_args = c.parse_args("--debug A --debug B --debug C")
    assert(parsed_args == {"debug": "C"})

def test_arg_parse_e() -> None:
    c : Command = Command()
    parsed_args = c.parse_args("A")
    assert(parsed_args == {})