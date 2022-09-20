from abc import ABC
from typing import List, Optional
from domain.entities import CourseCreate, CourseRead, CourseUpdate


class CourseRepository(ABC):
    def create(self, course: CourseCreate) -> CourseRead:
        raise NotImplementedError

    def read(self, slug: str) -> Optional[CourseRead]:
        raise NotImplementedError

    def read_all(self) -> List[CourseRead]:
        raise NotImplementedError

    def update(self, course: CourseUpdate) -> Optional[CourseRead]:
        raise NotImplementedError

    def delete(self, slug: str) -> Optional[CourseRead]:
        raise NotImplementedError
