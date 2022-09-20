from typing import List, Optional
from domain.entities import CourseCreate, CourseRead, CourseUpdate
from data.repos import CourseRepository
from utils import singleton, slugify


@singleton
class TestCourseRepository(CourseRepository):
    def __init__(self, *args, **kwargs):
        self._courses: List[CourseRead] = []

    def create(self, course: CourseCreate) -> CourseRead:
        new_course = CourseRead(
            **dict(
                slug=slugify(course.title),
                **course.dict(),
            ))
        self._courses.append(new_course)
        return new_course

    def read(self, slug: str) -> Optional[CourseRead]:
        for course in self._courses:
            if course.slug == slug:
                return course
        return None
    
    def read_all(self) -> List[CourseRead]:
        return self._courses
    
    def update(self, course: CourseUpdate) -> Optional[CourseRead]:
        for i, c in enumerate(self._courses):
            if c.slug == course.slug:
                self._courses[i] = course
                return course
        return None
    
    def delete(self, slug: str) -> Optional[CourseRead]:
        for i, c in enumerate(self._courses):
            if c.slug == slug:
                self._courses.pop(i)
                return c
        return None