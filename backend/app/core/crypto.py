"""
Módulo de criptografia - Funções para encriptação/decriptação de dados sensíveis
Utiliza Fernet (AES-128) do módulo cryptography
"""
import os
from typing import Optional
from cryptography.fernet import Fernet, InvalidToken


class CryptoManager:
    """Gerenciador de criptografia para campos sensíveis"""
    
    def __init__(self, key: Optional[str] = None):
        """
        Inicializa o gerenciador de criptografia
        
        Args:
            key: Chave de criptografia em base64. Se None, usa variável de ambiente ENCRYPTION_KEY
        """
        self.key = key or os.getenv("ENCRYPTION_KEY")
        
        if not self.key:
            # Em vez de gerar chave aleatória que corrompe o banco ao reiniciar, 
            # deriva uma chave válida a partir do SECRET_KEY
            import hashlib
            import base64
            from app.core.config import settings
            
            # Fernet precisa de 32 bytes base64 url-safe
            key_bytes = hashlib.sha256(settings.SECRET_KEY.encode()).digest()
            self.key = base64.urlsafe_b64encode(key_bytes).decode()
            
        self.cipher = Fernet(self.key.encode() if isinstance(self.key, str) else self.key)
    
    def encrypt(self, data: str) -> str:
        """
        Encripta uma string de dados
        
        Args:
            data: String a ser encriptada
            
        Returns:
            String encriptada em formato base64
        """
        if not data:
            return ""
        
        encrypted = self.cipher.encrypt(data.encode())
        return encrypted.decode()
    
    def decrypt(self, encrypted_data: str) -> str:
        """
        Decripta uma string de dados
        
        Args:
            encrypted_data: String encriptada em formato base64
            
        Returns:
            String decriptada
            
        Raises:
            InvalidToken: Se a chave estiver incorreta ou dados corrompidos
        """
        if not encrypted_data:
            return ""
        
        try:
            decrypted = self.cipher.decrypt(encrypted_data.encode())
            return decrypted.decode()
        except InvalidToken as e:
            raise ValueError(f"Falha ao decriptar dados: {str(e)}") from e
    
    def generate_key(self) -> str:
        """
        Gera uma nova chave de criptografia
        
        Returns:
            Chave em formato base64
        """
        return Fernet.generate_key().decode()


# Instância global do gerenciador de criptografia
_crypto_manager: Optional[CryptoManager] = None


def get_crypto_manager() -> CryptoManager:
    """
    Retorna instância global do gerenciador de criptografia
    
    Returns:
        CryptoManager singleton
    """
    global _crypto_manager
    if _crypto_manager is None:
        _crypto_manager = CryptoManager()
    return _crypto_manager


def encrypt_field(data: str) -> str:
    """Helper para encriptar um campo"""
    return get_crypto_manager().encrypt(data)


def decrypt_field(encrypted_data: str) -> str:
    """Helper para decriptar um campo"""
    return get_crypto_manager().decrypt(encrypted_data)
