from typing import List

from pydantic import BaseModel

from data_providers.repository_interfaces.TodoRepositoryInterface import (
    TodoRepositoryInterface,
)
from entities.TodoItem import TodoItem


class GetTodoAllResponse(BaseModel):
    id: str
    title: str
    is_completed: bool

    @staticmethod
    def from_entity(todo_item: TodoItem):
        return GetTodoAllResponse(id=todo_item.id, title=todo_item.title, is_completed=todo_item.is_completed)


def get_todo_all_use_case(
    user_id: str,
    todo_repository: TodoRepositoryInterface,
) -> List[GetTodoAllResponse]:
    return [
        GetTodoAllResponse.from_entity(todo_item)
        for todo_item in todo_repository.get_all()
        if todo_item.user_id == user_id
    ]
