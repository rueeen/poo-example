class BibliotecaError(Exception):
    """Error base de la aplicación."""


class AutenticacionError(BibliotecaError):
    """Error para problemas de autenticación/autorización."""


class OperacionBDNoAplicadaError(BibliotecaError):
    """Error cuando una operación SQL no afecta filas esperadas."""
