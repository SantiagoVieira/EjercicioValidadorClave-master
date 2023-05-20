# TODO: Implementa el código del ejercicio aquí
# NO ESTA COMPLETO, FALTA MAS IMPLEMENTACION Y CORRECCIONES
from abc import ABC, abstractmethod

class ValidationRule(ABC):
    def _init_(self, expected_length):
        self._expected_length = expected_length

    def _validate_length(self, password):
        if len(password) <= self._expected_length:
            raise InvalidLengthError()

    def _contains_uppercase(self, password):
        if not any(char.isupper() for char in password):
            raise MissingUppercaseError()

    def _contains_lowercase(self, password):
        if not any(char.islower() for char in password):
            raise MissingLowercaseError()

    def _contains_number(self, password):
        if not any(char.isdigit() for char in password):
            raise MissingNumberError()

    @abstractmethod
    def is_valid(self, password):
        pass


class GanimedesValidationRule(ValidationRule):
    def contains_special_character(self, password):
        special_characters = ['@', '_', '#', '$', '%']
        if not any(char in special_characters for char in password):
            raise MissingSpecialCharacterError()

    def is_valid(self, password):
        self._validate_length(password)
        self._contains_uppercase(password)
        self._contains_lowercase(password)
        self._contains_number(password)
        self.contains_special_character(password)
        return True


class CalistoValidationRule(ValidationRule):
    def contains_calisto(self, password):
        if password.find('calisto') == -1:
            raise InvalidCalistoError()

    def is_valid(self, password):
        self._validate_length(password)
        self._contains_number(password)
        self.contains_calisto(password)
        return True


class Validator:
    def _init_(self, rule):
        self.rule = rule

    def is_valid(self, password):
        return self.rule.is_valid(password)