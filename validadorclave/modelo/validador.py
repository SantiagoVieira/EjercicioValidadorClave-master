# TODO: Implementa el código del ejercicio aquí
# NO ESTA COMPLETO, FALTA MAS IMPLEMENTACION Y CORRECCIONES
from abc import ABC, abstractmethod
import errors

class ValidationRule(ABC):
    def __init__(self, expected_length):
        self._expected_length = expected_length

    def _validate_length(self, key):
        if len(key) <= self._expected_length:
            raise errors.MinLengthNotMetError()

    def _contains_uppercase(self, key):
        if not any(c.isupper() for c in key):
            raise errors.NoUppercaseLetterError()

    def _contains_lowercase(self, key):
        if not any(c.islower() for c in key):
            raise errors.NoLowercaseLetterError()

    def _contains_digit(self, key):
        if not any(c.isdigit() for c in key):
            raise errors.NoNumberError()

    @abstractmethod
    def is_valid(self, key):
        pass


class GanymedeValidationRule(ValidationRule):
    def _contains_special_character(self, key):
        special_characters = ['@', '_', '#', '$', '%']
        if not any(c in special_characters for c in key):
            raise errors.NoSpecialCharacterError()

    def is_valid(self, key):
        self._validate_length(key)
        self._contains_uppercase(key)
        self._contains_lowercase(key)
        self._contains_digit(key)
        self._contains_special_character(key)
        return True


class CallistoValidationRule(ValidationRule):
    def _contains_callisto(self, key):
        if key.find('callisto') == -1:
            raise errors.NoSecretWordError()

    def is_valid(self, key):
        self._validate_length(key)
        self._contains_digit(key)
        self._contains_callisto(key)
        return True


class Validator:
    def __init__(self, rule):
        self.rule = rule

    def is_valid(self, key):
        return self.rule.is_valid(key)


