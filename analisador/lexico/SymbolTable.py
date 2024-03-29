from analisador.lexico.Token import Token

class SymbolTable:
    def __init__(self):
        self.table: list[Token] = []

    def get_token(self, lexeme: str) -> Token | None:
        try:
            return [l for l in self.table if l.lexeme == lexeme][0]
        except IndexError:
            return None
    
    def insert_token(self, token: Token):
        self.table.append(token)

    def has_token(self, token) -> bool:
        return any(token_.lexeme == token.lexeme for token_ in self.table)

    def update_token_type(self, lexeme: str, type_name: str):
        if token := self.get_token(lexeme):
            token.type_name = type_name
        else:
            raise LookupError(f"Erro em update_token: Lexema '{lexeme}' não existe")
        
    def print(self):
        for token in self.table:
            print(f"Classe: {token.class_name}, Lexema: {token.lexeme}, Tipo: {token.type_name}")
