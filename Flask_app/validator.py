from pydantic import BaseModel, ValidationError
from typing import Type, Optional
from errors import HttpException


class PostArticleValidator(BaseModel):
    title: str
    description: str
    id_user: int


class PatchArticleValidator(BaseModel):
    id: int
    title: Optional[str]
    description: Optional[str]
    id_user: int


class DeleteArticleValidator(BaseModel):
    id: int
    id_user: int


def validate(data_to_validate: dict, validation_model: Type):
    try:
        model = validation_model(**data_to_validate)
        return model.dict(exclude_none=True)
    except ValidationError as error:
        raise HttpException(400, error.errors())

